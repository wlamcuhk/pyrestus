import pandas as pd
import numpy as np
import warnings
from pathlib import Path

def makeRaterDataFrame(folder:str, ignore_null:bool=True,
                       warning:bool=True)->pd.DataFrame:
    """
    Make pd.DataFrame from a directory containing Raters' rating.
    """

    dfs = []
    for f in Path(folder).iterdir():
        dfs.append(pd.DataFrame((file for file in sorted(f.iterdir())
                                 if not file.is_dir()), columns=[f.name]))

    main_df = pd.concat(dfs, axis=1)
    is_null = sum(main_df.isnull().values.any(axis=1))

    if ignore_null:
        main_df = main_df.dropna()

    if warning:
        if is_null > 0:
            warnings.warn(f"""{is_null} column(s) contain(s) empty values due to
                            unequal file numbers.""")
            if ignore_null:
                warnings.warn(f"{is_null} columns(s) have/has been dropped")

    return main_df


def inconsistentName(df:pd.DataFrame)->bool:
    """
    Check if every row contains the same file name.
    """
    assert not df.isnull().values.any(), \
    "DataFrame contains empty values. Please use .dropna() before name checking"

    return df.apply(lambda files : len(set([file.name for file in files])) > 1,
                    axis=1).values.any()

# TODO: modify this function
def color_values(val:float)->str:
    color = '' if val < 1.0 else 'green'
    return 'background-color: %s' % color