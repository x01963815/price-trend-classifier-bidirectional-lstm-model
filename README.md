# price-trend-classifier-bidirectional-lstm-model
使用 Tensorflow 建立 Bidirectional LSTM model 用於判斷股價處於何種趨勢中。目的是將訓練完成的模型用於自動標記其他股價趨勢。

## 資料匯入及預處理
----------------------
蒐集鴻海(2317)股票的分鐘開盤價格，期間從 2018-02-22 至 2018-03-21 ，一共 5054 筆資料，並以人工方式判斷各資料點價格之趨勢，將其標記為上升、持平、下跌三種趨勢，作為模型訓練標籤。

![2317price](https://i.imgur.com/XNmPVVt.png)

將輸入的資料分割成 TIMESTEPS=256 為一筆的 sliding window 資料，並且以 Trend 在 HALF_TIMESTEPS=128 作為該筆資料的標籤，

例如：
- 第1筆資料為 $X_{1}$, $X_{2}$, $X_{3}$, … , $X_{254}$, $X_{255}$, $X_{256}$，標籤就為 $Y_{128}$ 

- 第2筆資料為 $X_{2}$, $X_{3}$, $X_{4}$, … , $X_{255}$, $X_{256}$, $X_{257}$，標籤就為 $Y_{129}$

另外強調本模型的目的不在於預測未來的趨勢，而是用來判斷並標記過去資料的趨勢，用於未來模型的建立，因此本模型是以大約前後兩個小時來判斷該時間點的趨勢。

![Structure_of_Bidirectional_LSTM_model_of_Price_Classifier](https://sites.google.com/site/xliuforliu/home/Structure_of_Bidirectional_LSTM_model_of_Price_Classifier.JPG)

模型學習完成後的準確率有93.4%