# PLAID 2018
[下載網址](https://figshare.com/articles/dataset/PLAID_-_A_Voltage_and_Current_Measurement_Dataset_for_Plug_Load_Appliance_Identification_in_Households/10084619)

## 下載項目
![plaid 2018 下載項目](./img/plaid_download.png)

## 使用方法 
1. 將 `plaid_new_.hdf5` 、 `metadata_aggregated.json` 、 `metadata_submetered.json` 放在同一個資料夾。
2. 將 `plaid_2018.py` 內的路徑改成 `使用方法 1` 的資料夾路徑。
  ```python
  ## plaid_2018.py
  ########################################  修改成自己的路徑

  plaid_hdf5_path = r"D:\NILM\dataset\plaid\2018/plaid_new_.hdf5"
  aggregated_json_path=r"D:\NILM\dataset\plaid\2018/metadata_aggregated.json"
  submetered_json_path = r"D:\NILM\dataset\plaid\2018/metadata_submetered.json"

  ########################################
  ```
3. 使用 `plaid_2018.py` 的 `ReadPLAID_2018()`方法
```python
obj = ReadPLAID_2018()
## Aggregated
aggregated_waves, aggregated_infos = obj.getAggregated()

## Submetered
submetered_waves, submetered_infos = obj.getSubmetered()
```

## 數據格式介紹
### Aggregated
* aggregated_waves
  * 有 <b>575</b> 個聚合負載的電壓、電流波型
    取出第 n 個 聚合負載 的電壓、電流波型
    <br>ex: `voltage_wave, current_wave = aggregated_waves[n-1][0], aggregated_waves[n-1][1]`
* aggregated_infos
  *  
