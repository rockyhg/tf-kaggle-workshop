# Predicting Road Accident Risk (s5e10)
https://www.kaggle.com/competitions/playground-series-s5e10/overview

## 第1回 キックオフ＆ベースライン (2025-11-07)

### コンペ概要理解

- 目標: 異なる種類の道路における事故発生の可能性を予測する
- 評価指標: RMSE (Root Mean Squared Error)
- 回帰問題
- 目的変数: accident_risk
- データ:
  - オリジナルデータがある Simulated Roads Accident 自由に使ってよい

### データ確認

- ノートブック: `exp01-eda.ipynb`
- データセット構成
  - train.csv: 学習用データ。accident_risk が目的変数
  - test.csv: テスト用データ
  - sample_submission.csv: 提出用サンプルファイル
- 欠損値なし
- 可視化アイデア・施策
  - road_signs_present と public_road
  - accident_risk: カイ2乗分布ぽい
  - 目的変数に対するクロス集計
  - train / test の特徴量分布の違いを確認

### ベースライン作成

- ノートブック: `exp02-baseline.ipynb`
- モデル: LightGBM 回帰モデル
- 数値型のみ投入
- ハイパーパラメータ: デフォルト + num_leaves=16 に変更
- 結果
  - CV: 0.10602 / LB: 0.10599

### 実行環境の検討

- Kaggle Notebook
	- データセットのダウンロード、アップロードが不要
	- GPUが無料で使える
	- Submit時に頭から実行される
- Google Colab
	- GPUが無料で使える
	- Geminiが利用可能
- ローカル環境
	- メリット: 自由に環境構築ができる
	- デメリット: GPUが使えない場合がある、データセットのダウンロード、アップロードが必要

### 実行時間の測定

- ノートブック: `exp03-exe-time.ipynb`
- Kaggle Notebook (CPU): 1m 6s
- Kaggle Notebook (GPU): 58s
- Google Colab (CPU): 2m 0s
- Google Colab (GPU): 1m 47s
- ローカル環境 (M2 MacBook 2022): 19s

**考察**

- Kaggle/Colab (GPU):
  - 時間のかかるデータ転送（オーバーヘッド）が発生した
  - さらに、特徴量が4つしかないためGPUの並列処理が活きず、計算も非効率だった
- ローカル (M2 CPU):
  - ユニファイドメモリのおかげでデータ転送がゼロ
  - 特徴量が4つしかないタスクは、CPUで順番に処理する方がはるかに効率的であり、そのCPU自体の性能もM2が高い

### Next Steps
- EDAの深掘り
- CVの改善
- 特徴量エンジニアリング


## 第2回 特徴量エンジニアリング (2025-11-14)

### EDAの深掘り
- ノートブック: `exp04-eda2.ipynb`
- 数値型変数と目的変数の関係
  - 相関係数: curvature > speed_limit > num_reported_accidents > num_lanes
- カテゴリ変数と目的変数の関係
  - lighting: night の事故リスクが高め
  - weather: clear 以外の事故リスクが高め
  - time_of_day: 朝夕の事故リスクが高め
  - lighting, weather, time_of_day 間のクロス集計 → 同じ傾向

### ベースラインの改善
- ノートブック: `exp05-cv.ipynb`
- 精度はCVスコアで確認しているけど、推論は5番目のモデルだけ使っている<br>
→ 全foldモデルで推論して平均化する（8章 8-20：Tips⑨）
- 全カラム投入
- CV: 0.05611 / LB: 0.05587

### 特徴量エンジニアリング
- ターゲットの対数変換
  - ノートブック: `exp06-log.ipynb`
  - 目的変数に log1p を適用して学習
  - 予測値に expm1 を適用して元のスケールに戻す
  - CV: 0.05612 / LB: 0.05589
- オリジナルデータとの結合データで学習
  - ノートブック: `exp07-orig-data.ipynb`
  - オリジナルデータを読み込み、trainデータと結合
  - CV: 0.05511 / LB: 0.05590

### Next Steps
- Code/Discussionを参照して特徴量エンジニアリングを検討する


## 分析管理シート（簡易版）

| 実験 | ベース | CV | LB | Comments |
|-----|-------|----|----|----------|
| exp02 | - | 0.10602 | 0.10599 | ベースライン |
| exp05 | exp02 | 0.05611 | **0.05587** | 全カラム投入、CV改善 |
| exp06 | exp05 | 0.05612 | 0.05589 | 目的変数の対数変換 |
| exp07 | exp06 | 0.05511 | 0.05590 | オリジナルデータとの結合データで学習 |
| exp |  |  |  |  |
| exp |  |  |  |  |
| exp |  |  |  |  |
| exp |  |  |  |  |
| exp |  |  |  |  |


■
