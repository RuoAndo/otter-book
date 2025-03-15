#!/usr/bin/bash

# 作業ディレクトリを設定
WORKING_DIR="/mnt/d/otter-book/8puzzle/puzzle_outputs"

# 処理するファイルのリストを取得
FILES=("$WORKING_DIR"/*.in)

# ファイルが存在するかチェック
if [ ${#FILES[@]} -eq 0 ]; then
    echo "No .txt files found in $WORKING_DIR"
    exit 1
fi

# 各ファイルを処理
for FILE in "${FILES[@]}"; do
    echo "Processing: $FILE"

    # コマンドをバックグラウンドで実行 & プロセスID取得
    timeout 30s bash -c "./otter < \"$FILE\"" &
    PID=$!

    # 30秒以内に終了しなければ強制終了
    sleep 30
    if ps -p $PID > /dev/null; then
        echo "Timeout reached, terminating process: $FILE"
        kill -9 $PID
    fi

    wait $PID 2>/dev/null
done

echo "All files processed."
