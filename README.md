# label-studio-sample

## 手順

- label-studioでアノテーションを行い、`Export`ボタンから`JSON-MIN`フォーマットを選択しダウンロード
- `convert.py`でalpacaフォーマットに変更
- `tran_qlora.ipynb`の`dataset_name`をlocalのjsonファイル（`convert.py`の出力ファイル）に変更し、実行