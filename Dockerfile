# Dockerfile
FROM python:3.11-slim

# 作業ディレクトリの設定
WORKDIR /usr/src/app

# 依存関係のインストール (ルートに配置)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードのコピー
# srcフォルダごとコピーし、コンテナ内でも /usr/src/app/src となる
COPY src ./src 

# Pythonが src ディレクトリ内のモジュールを見つけられるように PYTHONPATH を設定
ENV PYTHONPATH=/usr/src/app:$PYTHONPATH

# アプリケーションが待ち受けるポートを指定
EXPOSE 8000

# コンテナ起動時のコマンド
# 実行ファイルは src/app.py になった
CMD ["python", "src/app.py"]
