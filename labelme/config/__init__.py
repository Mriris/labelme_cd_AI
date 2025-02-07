import os
import os.path as osp
import shutil

import yaml
from loguru import logger

here = osp.dirname(osp.abspath(__file__))


def update_dict(target_dict, new_dict, validate_item=None):
    for key, value in new_dict.items():
        if validate_item:
            validate_item(key, value)
        if key not in target_dict:
            logger.warning("Skipping unexpected key in config: {}".format(key))
            continue
        if isinstance(target_dict[key], dict) and isinstance(value, dict):
            update_dict(target_dict[key], value, validate_item=validate_item)
        else:
            target_dict[key] = value


# -----------------------------------------------------------------------------


def get_default_config():
    config_file = osp.join(osp.dirname(__file__), "default_config.yaml")  # 确保路径正确
    user_config_file = osp.join(osp.expanduser("~"), ".labelmerc")  # 用户配置文件路径

    # **删除旧的 .labelmerc，确保加载最新配置**
    if osp.exists(user_config_file):
        try:
            os.remove(user_config_file)
            print(f"🗑 已删除旧的配置文件: {user_config_file}")
        except Exception as e:
            print(f"❌ 删除 .labelmerc 失败: {e}")

    # **重新复制 default_config.yaml 到 .labelmerc**
    try:
        shutil.copy(config_file, user_config_file)
        print(f"✅ 复制 default_config.yaml 到 {user_config_file}")
    except Exception as e:
        print(f"❌ 复制失败: {e}")

    # **加载最新的配置**
    with open(config_file, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # print(f"✅ 加载 default_config.yaml: {config['canvas']['crosshair']}")  # 确保 polygon: true 被读取
    return config


def validate_config_item(key, value):
    if key == "validate_label" and value not in [None, "exact"]:
        raise ValueError(
            "Unexpected value for config key 'validate_label': {}".format(value)
        )
    if key == "shape_color" and value not in [None, "auto", "manual"]:
        raise ValueError(
            "Unexpected value for config key 'shape_color': {}".format(value)
        )
    if key == "labels" and value is not None and len(value) != len(set(value)):
        raise ValueError(
            "Duplicates are detected for config key 'labels': {}".format(value)
        )


def get_config(config_file_or_yaml=None, config_from_args=None):
    # 1. default config
    config = get_default_config()

    print(f"🔍 传入的 config_file_or_yaml: {config_file_or_yaml}")

    # 2. specified as file or yaml
    if config_file_or_yaml is not None:
        config_from_yaml = yaml.safe_load(config_file_or_yaml)
        # print(f"✅ 解析后的 YAML: {config_from_yaml}")  # 确保 YAML 被正确解析

        if not isinstance(config_from_yaml, dict):
            with open(config_from_yaml) as f:
                logger.info("Loading config file from: {}".format(config_from_yaml))
                config_from_yaml = yaml.safe_load(f)

        update_dict(config, config_from_yaml, validate_item=validate_config_item)

    # 3. command line argument or specified config file
    if config_from_args is not None:
        update_dict(config, config_from_args, validate_item=validate_config_item)

    # print(f"✅ 最终 config: {config['canvas']['crosshair']}")  # 确保 crosshair 解析正确
    return config

