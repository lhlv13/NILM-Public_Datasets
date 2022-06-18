# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:23:52 2022
讀取Plaid2018 數據集
@author: Yuyi
"""
import numpy as np
import h5py
import matplotlib.pyplot as plt
import json
import re
import time


class ReadPLAID_2018():
    """
    處理 plaid-2018的數據集
    Init Parameters
    -------------------
    plaid_hdf5_path : plaid_new_.hdf5 的路徑
    aggregated_json_path : metadata_aggregated.json 的路徑
    submetered_json_path : metadata_submetered.json
    
    
    Method
    -------------------
    * getAggregated() : 取得聚合波型的 I(wave[0])、V(wave[1]) 波型 和 標籤資料("datas"、"sampling_frequency"、"cost_time"、"house")
            return wave_list、  label_list
    
    * getSubmetered() : 取得單一附載的 I、V 波型 和 標籤資料("status"、"datas"、"sampling_frequency"、"cost_time"、"house")
            return wave_list、  label_list
            
    
    
    """
    def __init__(self, plaid_hdf5_path=r"D:\NILM\dataset\plaid\2018/plaid_new_.hdf5", \
                 aggregated_json_path=r"D:\NILM\dataset\plaid\2018/metadata_aggregated.json", \
                 submetered_json_path = r"D:\NILM\dataset\plaid\2018/metadata_submetered.json"):
        self.__all_data = h5py.File(plaid_hdf5_path)
        self.__aggregated_path = aggregated_json_path
        self.__submetered_path = submetered_json_path
    
    def __useProgress(self, current, total, name=""):
        percent = current / total
        print("\r"+"PLAID-2018 %s LOAD [%s%s]%.2f%%"%(name, "#"*int(20*percent), " "*int(20*(1-percent)), percent*100), end="")
        pass
    
    def getAggregated(self):
        ## 標籤資料
        with open(self.__aggregated_path, 'r') as f:
            labels = json.load(f)
            
            
        ## 取得 V, i 波型  輸出波型 (575, 2, 波的取樣數)
        waves_list = []
        info_list = []
        for i in range(1, 576):  ## 共576個波 不會變
            self.__useProgress(i, 575, "Aggregated")   ### 進度條
            iv_wave = np.array(self.__all_data["aggregated"][str(i)]).T
            vi_wave = np.array([iv_wave[1], iv_wave[0]])
            waves_list.append(vi_wave)
            
            
            ## 波型的標籤資料
            label = labels[str(i)]
            label_dict = {}
            label_list = []
            name_list = []
            event_list = []
            
            for j in range(len(label["appliances"])):
                on = re.search("\[(.+)\]", label["appliances"][j]["on"]).group(1).split()
                on = [int(on[0])] if len(on)==1 else [int(on[0]), int(on[1])]
                
                try:
                    off = int(label["appliances"][j]["off"].split("]")[0].split("[")[-1])
                except:
                    off = -1
                appliance = label["appliances"][j]["type"]
                label_list.append([on, int(off), appliance])
                name_list.append(appliance)
                
                ## 特別另外儲存事件(不分on off)
                if len(on)>1:
                    event_list.append(on[0])
                    event_list.append(on[1])
                    event_list.append(off)
                else:
                    event_list.append(on[0])
                    event_list.append(off)
                    
            event_list.sort()
            frequency = int(label["header"]["sampling_frequency"].replace("Hz", ""))
            cost_time = int(label["instances"]["length"].split(".")[0])
            house = label["location"]
            
            ## 放入 label_dict
            label_dict["datas"] = label_list   ## 內含較完整的訊息 [[on], off, 事件設備]
            label_dict["labels"] = name_list   ## 只存 事件的設備名稱們
            label_dict["events"] = event_list  ## 儲存所有事件(on、off放一起)
            label_dict["sampling_frequency"] = frequency
            label_dict["cost_time"] = cost_time
            label_dict["house"] = house
            
            ## 放入 info_list
            info_list.append(label_dict)
        print("")   ## 讓進度條完成後的下一個輸入可以在下一行
        return waves_list, info_list
    
    def getSubmetered(self):
        ## 標籤資料
        with open(self.__submetered_path, 'r') as f:
            labels = json.load(f)
        
        ## 取得 V, i 波型  輸出波型 (575, 2, 波的取樣數)
        waves_list = []
        info_list = []
        for i in range(1, 1877):  ## 共1876個波 不會變
            self.__useProgress(i, 1876, "Submetered")    ### 進度條
            iv_wave = np.array(self.__all_data["submetered"][str(i)]).T
            vi_wave = np.array([iv_wave[1], iv_wave[0]])
            waves_list.append(vi_wave)
            
            ## 波型的標籤資料
            label = labels[str(i)]
            label_dict = {}
            
            label_name = label["appliance"]["type"]
            label_status = label["appliance"]["status"]
            frequency = int(label["header"]["sampling_frequency"].replace("Hz", ""))
            cost_time = int(label["instances"]["length"].split(".")[0])
            house = label["location"]
            
            
            ## 放入 label_dict
            label_dict["label"] = label_name
            label_dict["status"] = label_status
            label_dict["sampling_frequency"] = frequency
            label_dict["cost_time"] = cost_time
            label_dict["house"] = house
            
            info_list.append(label_dict)
        print("")   ## 讓進度條完成後的下一個輸入可以在下一行
        return waves_list, info_list




def main():
    waves, labels = ReadPLAID_2018().getAggregated()    
    
    
    for i in range(len(waves)):
        events = labels[i]["events"]
    
        

if __name__ == "__main__":
    main()