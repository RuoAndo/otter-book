# 作業ディレクトリを設定
$workingDir = "D:\otter-book\8puzzle\puzzle_outputs"

# すべてのテキストファイルを取得
$files = Get-ChildItem -Path $workingDir -Filter "*.txt"

foreach ($file in $files) {
    $filePath = $file.FullName
    Write-Host "Processing: $filePath"

    # コマンドの実行
    $process = Start-Process -FilePath "cmd.exe" -ArgumentList "/c .\otter < `"$filePath`"" -NoNewWindow -PassThru

    # 最大 30 秒待機
    $process | Wait-Process -Timeout 30 -ErrorAction SilentlyContinue

    # タイムアウトした場合は強制終了
    if (!$process.HasExited) {
        Write-Host "Timeout reached, terminating process: $filePath"
        Stop-Process -Id $process.Id -Force
    }
}
Write-Host "All files processed."
