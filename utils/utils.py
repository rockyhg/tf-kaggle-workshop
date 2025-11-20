import logging
from time import time

import pandas as pd


def check_df(df, columns=None, show_values_limit=10):
    """
    DataFrameの各列の情報（データ型、NaN数、ユニーク数、ユニーク値）を一覧表示します

    Parameters:
    - df: 対象のDataFrame
    - columns: 対象の列 (list)。Noneのときは全列
    - show_values_limit: ユニーク値を表示する最大数。これを超える列は「多すぎる」と表示されます

    Returns:
    - info_df: 各列の情報をまとめたDataFrame
    """
    if columns is not None:
        df = df[columns]

    type_series = df.dtypes
    nan_count_series = df.isnull().sum()
    nunique_series = df.nunique()

    unique_values = {}
    for col in df.columns:
        if nunique_series[col] <= show_values_limit:
            unique_values[col] = df[col].unique().tolist()
        else:
            unique_values[col] = f"> {show_values_limit} unique values"

    info_df = pd.DataFrame(
        {
            "dtypes": type_series.astype(str),
            "NaN Count": nan_count_series,
            "Nunique": nunique_series,
            "Unique Values": pd.Series(unique_values),
        }
    )

    info_df = info_df.reset_index().rename(columns={"index": "Column"})

    return info_df


def elapsed_time(start):
    """経過時間を表示する関数
    Args:
        start (float): 開始時刻
    """
    elapsed = int(time() - start)
    minutes, elapsed = divmod(elapsed, 60)
    hours, minutes = divmod(minutes, 60)
    seconds = elapsed % 60
    return hours, minutes, seconds


def setup_logger(name="run", level=logging.INFO):
    """ロガーを設定する関数
    Args:
        name (str): ロガーの名前
        level (int): ログレベル
    Returns:
        logging.Logger: 設定されたロガー
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    if not logger.handlers:
        # コンソール出力
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        # ファイル出力
        log_file = f"{name}.log"
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
