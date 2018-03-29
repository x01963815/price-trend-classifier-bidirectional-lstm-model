# price-trend-classifier-bidirectional-lstm-model
使用 Tensorflow 建立 Bidirectional LSTM model 用於判斷股價處於何種趨勢中。目的是將訓練完成的模型用於自動標記其他股價趨勢。

### 詳細模型內容請參考 bidirectional_lstm_model.ipynb

## 資料來源
----------------------
蒐集鴻海(2317)股票的分鐘開盤價格，期間從 2018-02-22 至 2018-03-21 ，一共 5054 筆資料，並以人工方式判斷各資料點價格之趨勢，將其標記為上升、持平、下跌三種趨勢，作為模型訓練標籤。

![2317price](https://i.imgur.com/XNmPVVt.png)

另外強調本模型的目的不在於預測未來的趨勢，而是用來判斷並標記過去資料的趨勢，用於未來模型的建立，因此本模型是以大約前後兩個小時來判斷該時間點的趨勢。

## 模型結構
-------------------------
將輸入的資料分割成 256 為一筆的 sliding window 資料，並且以 Trend 在128 作為該筆資料的標籤

![Structure_of_Bidirectional_LSTM_model_of_Price_Classifier](https://sites.google.com/site/xliuforliu/home/Structure_of_Bidirectional_LSTM_model_of_Price_Classifier.JPG)

## 模型結果
--------------------------
### Accuracy of Minibatch
![accuracy](https://i.imgur.com/B3jOafx.png)

### Loss of Minibatch
![loss](https://i.imgur.com/kU1dkL0.png)

模型學習完成後的準確率為 93.4%

## 未來方向
-------------------------
此模型還有修改空間，將來可以朝幾個方向修改：
1. 增加訓練的資料量
2. 加入指數衰減學習率
3. 增加 LSTM 隱藏結點數量或增加隱藏層
4. 以CNN模型處理類似問題

為了提高模型的實用性，未來應減少判斷趨勢時使用的時間長度，目前是使用前後2個小時，未來模型應減少至1個小時或更短。