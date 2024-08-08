# 🚀 IRIS

## 📋 概要

IRISは、GitHubリポジトリのイシュー管理を自動化するインテリジェントアシスタントです。機械学習と自然言語処理を活用し、イシューの自動分類、優先順位付け、解決策の提案を行います。

## ✨ 主な機能

- イシューの自動ラベリング
- 複数のAIモデルを活用したイシュー分析
- GitHubアクションを通じた自動化プロセス
- カスタマイズ可能なラベル管理
- 詳細なコメント生成
- 変更提案
- 自動リリースノート生成

## 🆕 最新情報

- **v0.5.0:** リリースノートの自動生成、READMEの自動更新、ヘッダー画像の生成など、新たな機能が追加されました。

## 🛠️ インストール手順

1. **リポジトリのクローン:**
   - GitHubリポジトリをクローンします。
   ```bash
   git clone https://github.com/Sunwood-ai-labs/IRIS.git
   ```
2. **ワークフローファイルのコピー:**
   - リポジトリ内の `.github/workflows/` ディレクトリにある全てのYAMLファイルを、あなたのGitHubリポジトリの `.github/workflows/` ディレクトリにコピーします。
3. **GitHubシークレットの設定:**
   - GitHubリポジトリの「Settings」タブから「Secrets and variables」→「Actions」を選択し、以下のシークレットを追加します：
     - `GITHUB_TOKEN`: GitHubのパーソナルアクセストークン
     - `GEMINI_API_KEY`: Google AI StudioのAPIキー
     - `YOUR_PERSONAL_ACCESS_TOKEN`: GitHubのパーソナルアクセストークン（リポジトリへの書き込み権限が必要）
     - `YOUR_PERSONAL_ACCESS_TOKEN_IRIS`: IRISシステム用の特別なパーソナルアクセストークン
4. **依存関係のインストール:**
   - `requirements.txt` ファイルに記載された依存関係をインストールします。
   ```bash
   pip install -r requirements.txt
   ```

## 📄 ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

## ❓ ヘルプとサポート

質問やサポートが必要な場合は、[GitHubのIssues](https://github.com/Sunwood-ai-labs/IRIS/issues)ページで新しいイシューを作成してください。

## 🤝 コントリビューション

プロジェクトへの貢献は大歓迎です！

- イシューを作成して改善点や問題点を報告
- 新機能の提案
- プルリクエストを送信してコードを改善

初めての方は、[First Contributions](https://github.com/firstcontributions/first-contributions) のガイドを参考にしてみてください。