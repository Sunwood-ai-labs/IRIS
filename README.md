<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/IRIS.png" width="100%">
<br>
<h1 align="center">IRIS</h1>
<h2 align="center">
  ～ Intelligent Repository Issue Solver ～
<br>

<a href="https://github.com/Sunwood-ai-labs/IRIS" title="Go to GitHub repo"><img src="https://img.shields.io/static/v1?label=IRIS&message=Sunwood-ai-labs&color=blue&logo=github"></a>
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/IRIS">
<a href="https://github.com/Sunwood-ai-labs/IRIS"><img alt="forks - Sunwood-ai-labs" src="https://img.shields.io/github/forks/IRIS/Sunwood-ai-labs?style=social"></a>
<a href="https://github.com/Sunwood-ai-labs/IRIS"><img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/Sunwood-ai-labs/IRIS"></a>
<a href="https://github.com/Sunwood-ai-labs/IRIS"><img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/Sunwood-ai-labs/IRIS"></a>
<img alt="GitHub Release" src="https://img.shields.io/github/v/release/Sunwood-ai-labs/IRIS?color=red">
<img alt="GitHub Tag" src="https://img.shields.io/github/v/tag/Sunwood-ai-labs/IRIS?sort=semver&color=orange">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/IRIS/publish-to-pypi.yml">
<br>
<p align="center">
  <a href="https://hamaruki.com/"><b>[🌐 Website]</b></a> •
  <a href="https://github.com/Sunwood-ai-labs"><b>[🐱 GitHub]</b></a>
  <a href="https://x.com/hAru_mAki_ch"><b>[🐦 Twitter]</b></a> •
  <a href="https://hamaruki.com/"><b>[🍀 Official Blog]</b></a>
</p>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリのリリースノートやREADME、コミットメッセージの9割近くは[claude.ai](https://claude.ai/)や[ChatGPT4](https://chatgpt.com/)を活用した[AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II)で生成しています。

## 🌟 はじめに

I.R.I.S（Intelligent Repository Issue Solver）は、GitHubリポジトリのイシュー管理を劇的に向上させるインテリジェントアシスタントです。機械学習と自然言語処理を活用し、イシューの自動分類、優先順位付け、解決策の提案を行います。

初めての方でも簡単に使い始められるよう、以下では詳しい説明と手順を記載しています。

## 🚀 機能

- イシューの自動ラベリング：新しいイシューが作成されると、AIがその内容を分析し、適切なラベルを自動的に付与します。
- 複数のAIモデルを活用したイシュー分析：Google Gemini AIなど、高度な自然言語処理モデルを用いて、イシューの内容を深く理解します。
- GitHubアクションを通じた自動化プロセス：人間の介入なしに、24時間365日稼働します。
- カスタマイズ可能なラベル管理：CSVファイルを通じて、プロジェクト固有のラベルを簡単に定義・管理できます。
- 詳細なコメント生成：イシューに対して深い洞察を提供する詳細なコメントを自動生成します。
- 変更提案：イシューに基づいて具体的な変更提案を生成し、プルリクエストの作成をサポートします。
- 自動リリースノート生成：プルリクエストのマージ時に、AIを使用して自動的にリリースノートを生成します。

## 今後の実装項目

- ✅タグ付与で自動リリースノート作成開始
- ✅リリースノートの作成時にREADMEを自動更新
- ✅READMEが更新されると同時に英語版README作成

## 📁 リポジトリ構造

```bash
IRIS/
├─ .github/
│  ├─ scripts/
│  │  ├─ deep_comment.py
│  │  ├─ suggest_changes.py
│  │  ├─ label_adder.py
│  │  └─ generate_github_release_notes.py
│  ├─ workflows/
│  │  ├─ issue-deep-comment.yml
│  │  ├─ issue-review.yml
│  │  └─ generate-release-notes.yml
│  ├─ services/
│  │  └─ github_service.py
│  └─ config.py
├─ docs/
│  └─ .sourcesage_releasenotes.yml
└─ README.md
```

## 🛠️ インストールと設定（初心者向けステップバイステップガイド）

1. **リポジトリのクローン**:
   - GitHubアカウントをお持ちでない場合は、まず[GitHubに登録](https://github.com/join)してください。
   - [IRIS リポジトリ](https://github.com/Sunwood-ai-labs/IRIS)にアクセスし、緑色の「Code」ボタンをクリックします。
   - 「Download ZIP」を選択してファイルをダウンロードし、解凍します。

2. **ワークフローファイルのコピー**:
   - 解凍したフォルダ内の `.github/workflows/` ディレクトリにある全てのYAMLファイルを見つけます。
   - これらのファイルをあなたのGitHubリポジトリの `.github/workflows/` ディレクトリにコピーします。
     （`.github/workflows/` ディレクトリがない場合は作成してください）

3. **GitHubシークレットの設定**:
   - GitHubリポジトリのページで「Settings」タブをクリックします。
   - 左側のメニューから「Secrets and variables」→「Actions」を選択します。
   - 「New repository secret」ボタンをクリックし、以下のシークレットを追加します：
     - `GITHUB_TOKEN`: GitHubのパーソナルアクセストークン
     - `GEMINI_API_KEY`: Google AI StudioのAPIキー
     - `YOUR_PERSONAL_ACCESS_TOKEN`: GitHubのパーソナルアクセストークン（リポジトリへの書き込み権限が必要）
     - `YOUR_PERSONAL_ACCESS_TOKEN_IRIS`: IRISシステム用の特別なパーソナルアクセストークン
   - これらのキーの取得方法が分からない場合は、各サービスのドキュメントを参照するか、開発者に相談してください。

4. **依存関係のインストール**:
   - `requirements.txt` ファイルに記載された依存関係をインストールします。
   ```
   pip install -r requirements.txt
   ```

## 🔧 使用方法

IRISを設定したら、以下のように動作します：

1. あなたのリポジトリに新しいイシューが作成されると、IRISが自動的に起動します。
2. AIがイシューの内容を分析します。
3. 適切なラベルが提案され、自動的にイシューに適用されます。
4. 詳細なコメントがイシューに追加されます。
5. 必要に応じて、変更提案が生成されます。
6. プルリクエストがマージされると、自動的にリリースノートが生成されます。

特別な操作は必要ありません。新しいイシューを作成するだけで、IRISが自動的に処理を行います。

## 📝 更新情報

- [v0.4.0](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.4.0): 自動リリースノート生成機能の追加、GitHub Serviceの改善
- [v0.3.0](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.3.0): 詳細コメント生成機能、変更提案機能の追加
- [v0.2.0](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.2.0): Google Generative AI統合、ラベル管理システムの改善、ユーザビリティの向上
- [v0.1.0](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.1.0): イシュー自動ラベリング機能の実装

## 🔄 ワークフロー

IRISの動作フローを以下の図で説明します：

```mermaid
%%{init:{'theme':'base','themeVariables':{'primaryColor':'#024959','primaryTextColor':'#F2C335','primaryBorderColor':'#F2AE30','lineColor':'#A1A2A6','secondaryColor':'#593E25','tertiaryColor':'#F2C335','noteTextColor':'#024959','noteBkgColor':'#F2C335','textColor':'#024959','fontSize':'18px'}}}%%

sequenceDiagram
    participant User as 👤 User
    participant GitHub as 🐙 GitHub
    participant IRIS as 🤖 I.R.I.S
    participant AI as 🧠 AI Models
    participant Labels as 📋 Labels

    alt イシュー作成フェーズ
        User->>GitHub: イシューを作成
        GitHub->>IRIS: GitHub Action トリガー
    end

    alt イシュー分析フェーズ
        IRIS->>GitHub: イシュー内容を取得
        GitHub-->>IRIS: イシュー詳細
        IRIS->>AI: 内容を分析リクエスト
        AI-->>IRIS: 分析結果
    end

    alt ラベリングフェーズ
        IRIS->>Labels: 提案されたラベルを照合
        Labels-->>IRIS: 有効なラベル
        IRIS->>GitHub: 検証済みラベルを適用
    end

    alt コメント生成フェーズ
        IRIS->>AI: 詳細コメント生成リクエスト
        AI-->>IRIS: 生成された詳細コメント
        IRIS->>GitHub: 詳細コメントを追加
    end

    alt 変更提案フェーズ
        IRIS->>AI: 変更提案生成リクエスト
        AI-->>IRIS: 生成された変更提案
        IRIS->>GitHub: 変更提案を追加
    end

    alt リリースノート生成フェーズ
        GitHub->>IRIS: プルリクエストマージ通知
        IRIS->>AI: リリースノート生成リクエスト
        AI-->>IRIS: 生成されたリリースノート
        IRIS->>GitHub: リリースノートを作成
    end

    GitHub-->>User: 更新通知
```

## 🧪 開発用コマンド（上級者向け）

IRISの開発に携わる方向けのコマンドです：

AIRAを使用してコミットメッセージを生成：
```bash
aira --mode sourcesage commit  --config=.aira\config.dev.commit.yml --ss-model-name="gemini/gemini-1.5-pro-latest" --llm-output="llm_output.md"
```

SourceSageを使用してリリースノートを生成：
```bash
sourcesage --ss-mode=DocuMind --yaml-file=docs\.sourcesage_releasenotes.yml
```

## 🤝 コントリビューション

プロジェクトへの貢献を歓迎します！以下の方法で貢献できます：

1. イシューを作成して改善点や問題点を報告
2. 新機能の提案
3. プルリクエストを送信してコードを改善

初めての方は、[First Contributions](https://github.com/firstcontributions/first-contributions) のガイドを参考にしてみてください。

## 📄 ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。使用、複製、変更、配布の際はライセンス条項をご確認ください。

## 🙏 謝辞

- Google - Gemini AIの提供
- GitHub - アクションと開発プラットフォームの提供
- すべてのコントリビューターとユーザーの皆様

## ❓ ヘルプとサポート


質問やサポートが必要な場合は、以下の方法でお問い合わせください：

1. [GitHubのIssues](https://github.com/Sunwood-ai-labs/IRIS/issues)ページで新しいイシューを作成
2. [公式ウェブサイト](https://hamaruki.com/)のお問い合わせフォームを利用
3. [Twitter](https://x.com/hAru_mAki_ch)でダイレクトメッセージを送信

初心者の方も気軽にお問い合わせください。皆様のフィードバックをお待ちしています！
