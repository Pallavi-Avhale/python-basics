# PROPERTIES OF PANDA SERIES --->


# | Property  | Meaning                   | Syntax      | Example            |
# | --------- | ------------------------- | ----------- | ------------------ |
# |  index    | Shows index labels        | `s.index`   | `print(s.index)`   |
# |  values   | Returns data values       | `s.values`  | `print(s.values)`  |
# |  dtype    | Shows datatype            | `s.dtype`   | `print(s.dtype)`   |
# |  shape    | Returns shape             | `s.shape`   | `print(s.shape)`   |
# |  size`    | Number of elements        | `s.size`    | `print(s.size)`    |
# |  ndim`    | Number of dimensions      | `s.ndim`    | `print(s.ndim)`    |
# |  empty`   | Checks if Series is empty | `s.empty`   | `print(s.empty)`   |
# |  name`    | Returns series name       | `s.name`    | `print(s.name)`    |
# |  hasnans` | Checks missing values     | `s.hasnans` | `print(s.hasnans)` |
# |  T`       | Transpose                 | `s.T`       | `print(s.T)`       |
# |  axes`    | Returns axis labels       | `s.axes`    | `print(s.axes)`    |


# Series Methods
# Head & Tail Methods

# | Method   | Meaning      | Syntax     | Example           |
# | -------- | ------------ | ---------- | ----------------- |
# |  head()  | First 5 rows |  s.head()  |  print(s.head())  |
# |  tail()  | Last 5 rows  |  s.tail()  |  print(s.tail())  |

# Information Methods
# | Method           | Meaning                  | Syntax             | Example                   |
# | ---------------- | ------------------------ | ------------------ | ------------------------- |
# | `describe()`     | Statistical summary      | `s.describe()`     | `print(s.describe())`     |
# | `info()`         | Information about series | `s.info()`         | `s.info()`                |
# | `count()`        | Count non-null values    | `s.count()`        | `print(s.count())`        |
# | `unique()`       | Unique values            | `s.unique()`       | `print(s.unique())`       |
# | `nunique()`      | Number of unique values  | `s.nunique()`      | `print(s.nunique())`      |
# | `value_counts()` | Frequency count          | `s.value_counts()` | `print(s.value_counts())` |

# Mathematical Methods

# | Method      | Meaning             | Syntax        | Example              |
# | ----------- | ------------------- | ------------- | -------------------- |
# | `sum()`     | Sum of values       | `s.sum()`     | `print(s.sum())`     |
# | `mean()`    | Average             | `s.mean()`    | `print(s.mean())`    |
# | `median()`  | Middle value        | `s.median()`  | `print(s.median())`  |
# | `mode()`    | Most repeated value | `s.mode()`    | `print(s.mode())`    |
# | `min()`     | Minimum value       | `s.min()`     | `print(s.min())`     |
# | `max()`     | Maximum value       | `s.max()`     | `print(s.max())`     |
# | `std()`     | Standard deviation  | `s.std()`     | `print(s.std())`     |
# | `var()`     | Variance            | `s.var()`     | `print(s.var())`     |
# | `prod()`    | Product of values   | `s.prod()`    | `print(s.prod())`    |
# | `cumsum()`  | Cumulative sum      | `s.cumsum()`  | `print(s.cumsum())`  |
# | `cumprod()` | Cumulative product  | `s.cumprod()` | `print(s.cumprod())` |


# Sorting Methods

# | Method          | Meaning       | Syntax            | Example                  |
# | --------------- | ------------- | ----------------- | ------------------------ |
# | `sort_values()` | Sort values   | `s.sort_values()` | `print(s.sort_values())` |
# | `sort_index()`  | Sort by index | `s.sort_index()`  | `print(s.sort_index())`  |

# Missing Value Methods

# | Method      | Meaning               | Syntax        | Example              |
# | ----------- | --------------------- | ------------- | -------------------- |
# | `isnull()`  | Check null values     | `s.isnull()`  | `print(s.isnull())`  |
# | `notnull()` | Check non-null values | `s.notnull()` | `print(s.notnull())` |
# | `dropna()`  | Remove null values    | `s.dropna()`  | `print(s.dropna())`  |
# | `fillna()`  | Fill null values      | `s.fillna(0)` | `print(s.fillna(0))` |

# Indexing & Selection Methods

# | Method       | Meaning                  | Syntax      | Example            |
# | ------------ | ------------------------ | ----------- | ------------------ |
# | `loc[]`      | Label-based selection    | `s.loc[0]`  | `print(s.loc[0])`  |
# | `iloc[]`     | Position-based selection | `s.iloc[1]` | `print(s.iloc[1])` |
# | `getitem []` | Access element           | `s[0]`      | `print(s[0])`      |

# Conversion Methods

# | Method       | Meaning               | Syntax            | Example                  |
# | ------------ | --------------------- | ----------------- | ------------------------ |
# | `astype()`   | Change datatype       | `s.astype(float)` | `print(s.astype(float))` |
# | `tolist()`   | Convert to list       | `s.tolist()`      | `print(s.tolist())`      |
# | `to_dict()`  | Convert to dictionary | `s.to_dict()`     | `print(s.to_dict())`     |
# | `to_frame()` | Convert to DataFrame  | `s.to_frame()`    | `print(s.to_frame())`    |

# String Methods

# | Method           | Meaning           | Syntax                   | Example                         |
# | ---------------- | ----------------- | ------------------------ | ------------------------------- |
# | `str.upper()`    | Convert uppercase | `s.str.upper()`          | `print(s.str.upper())`          |
# | `str.lower()`    | Convert lowercase | `s.str.lower()`          | `print(s.str.lower())`          |
# | `str.contains()` | Search string     | `s.str.contains('a')`    | `print(s.str.contains('a'))`    |
# | `str.replace()`  | Replace text      | `s.str.replace('a','x')` | `print(s.str.replace('a','x'))` |
# | `str.len()`      | Length of string  | `s.str.len()`            | `print(s.str.len())`            |

# Boolean & Condition Methods

# | Method      | Meaning               | Syntax             | Example                   |
# | ----------- | --------------------- | ------------------ | ------------------------- |
# | `between()` | Check range           | `s.between(10,20)` | `print(s.between(10,20))` |
# | `isin()`    | Check values exist    | `s.isin([10,20])`  | `print(s.isin([10,20]))`  |
# | `where()`   | Conditional filtering | `s.where(s>20)`    | `print(s.where(s>20))`    |

# Apply & Map Methods

# | Method    | Meaning        | Syntax          | Example                 |
# | --------- | -------------- | --------------- | ----------------------- |
# | `apply()` | Apply function | `s.apply(func)` | `s.apply(lambda x:x*2)` |
# | `map()`   | Map values     | `s.map(dict)`   | `s.map({1:'A'})`        |