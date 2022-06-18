# PLAID 2018
[下載網址](https://figshare.com/articles/dataset/PLAID_-_A_Voltage_and_Current_Measurement_Dataset_for_Plug_Load_Appliance_Identification_in_Households/10084619)

## 下載項目
![plaid 2018 下載項目](./img/plaid_download.png)

## 使用方法 
1. 將 `plaid_new_.hdf5` 、 `metadata_aggregated.json` 、 `metadata_submetered.json` 放在同一個資料夾。
2. 將 `plaid_2018.py` 內的路徑改成 `使用方法 1` 的資料夾路徑。
```python
########################################  修改成自己的路徑

plaid_hdf5_path = r"D:\NILM\dataset\plaid\2018/plaid_new_.hdf5"
aggregated_json_path=r"D:\NILM\dataset\plaid\2018/metadata_aggregated.json"
submetered_json_path = r"D:\NILM\dataset\plaid\2018/metadata_submetered.json"

########################################
```


