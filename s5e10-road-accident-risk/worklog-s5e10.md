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

### Next Steps
- EDAの深掘り
- CVの改善
- 特徴量エンジニアリング

## 第2回 特徴量エンジニアリング (2025-11-14)
- 分析管理シート:


## 第3回 xxx (2025-11-21)


〓
