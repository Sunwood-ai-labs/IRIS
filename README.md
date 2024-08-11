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
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/iris-coon">
<img alt="PyPI - Format" src="https://img.shields.io/pypi/format/iris-coon">
<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/iris-coon">
<img alt="PyPI - Status" src="https://img.shields.io/pypi/status/iris-coon">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/iris-coon">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/iris-coon">
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
- READMEの自動更新：新しいリリースが発生すると、リリースノートの内容をREADMEに反映します。
- タグ付与での自動リリースノート作成：タグが付与されると、そのタグに対応するリリースノートが自動的に作成されます。
- 英語README作成：READMEが更新されると、同時に英語版READMEが作成されます。

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

## 🛠️ セットアップ方法

IRISは以下の2つの方法でセットアップできます：

1. **iris-coonコマンドを使用する方法**

   IRISをセットアップする最も簡単な方法は、`iris-coon`コマンドを使用することです。以下のコマンドでインストールとセットアップができます：

   ```bash
   pip install iris-coon
   iris-coon
   ```

   このコマンドを実行すると、必要なファイルとフォルダが現在のディレクトリにコピーされます。

2. **手動で.githubフォルダをコピーする方法**

   IRISの機能を既存のプロジェクトに追加したい場合は、以下の手順で.githubフォルダを直接コピーできます：

   ```bash
   git clone https://github.com/Sunwood-ai-labs/IRIS.git
   cp -r IRIS/.github /path/to/your/project/
   ```

   この方法では、IRISの.githubフォルダとその内容が、指定したプロジェクトディレクトリにコピーされます。必要に応じて、コピーしたファイルを編集してプロジェクトに合わせてカスタマイズできます。

### 🔐 GitHubシークレットの設定

どちらのセットアップ方法を選択した場合も、IRISを正常に機能させるために以下のGitHubシークレットを設定する必要があります：

1. GitHubリポジトリのページで「Settings」タブをクリックします。
2. 左側のメニューから「Secrets and variables」→「Actions」を選択します。
3. 「New repository secret」ボタンをクリックし、以下のシークレットを追加します：
   - `GITHUB_TOKEN`: GitHubのパーソナルアクセストークン
   - `GEMINI_API_KEY`: Google AI StudioのAPIキー
   - `YOUR_PERSONAL_ACCESS_TOKEN`: GitHubのパーソナルアクセストークン（リポジトリへの書き込み権限が必要）
   - `YOUR_PERSONAL_ACCESS_TOKEN_IRIS`: IRISシステム用の特別なパーソナルアクセストークン

これらのキーの取得方法については、各サービスのドキュメントを参照するか、開発者に相談してください。

### 💻 Pythonライブラリとしての使用

IRISをPythonライブラリとして使用したい場合は、`example/demo.py`ファイルを参考にしてください。このデモファイルには、IRISの主要な機能を使用する方法が示されています。

例えば：

```python
from iris_coon import IrisCoon

# IRISのセットアップ
coon = IrisCoon(target_dir="path/to/your/project", force=True)
coon.run()
```

詳細な使用方法と高度な設定については、`example/demo.py`ファイルを確認してください。

## 🔧 使用方法

IRISをセットアップすると、以下の自動化された機能が利用可能になります：

1. **イシュー管理の自動化**:
   - 新しいイシューが作成されると、IRISが自動的に起動します。
   - AIがイシューの内容を分析し、適切なラベルを提案・適用します。
   - イシューに詳細なコメントが自動追加されます。
   - 必要に応じて、コードの変更提案が生成されます。

2. **リリース管理の自動化**:
   - タグが付与されると、そのタグに対応する自動リリースノートが生成されます。
   - 新しいリリースが発生すると、READMEが自動更新されます。

3. **ドキュメンテーションの自動化**:
   - READMEが更新されると、自動的に英語版README（`README.en.md`）が生成されます。

### 🏷️ タグによる自動リリースノート生成

新しいバージョンをリリースする準備ができたら、以下のようにタグを付けるだけです：

```bash
git tag v1.0.0
git push origin v1.0.0
```

これにより、`v1.0.0`に対応する詳細なリリースノートが自動的に生成されます。

### 📝 READMEの自動更新と翻訳

1. リリースノートが生成されると、IRISはREADMEを自動更新し、新機能や重要な変更点を反映します。

2. その後、更新されたREADMEの内容に基づいて、英語版の`README.en.md`が自動生成されます。

### 🔄 継続的な改善

これらの自動化プロセスにより、以下のメリットが得られます：

- プロジェクトドキュメントが常に最新状態に保たれます。
- 開発者の作業負荷が大幅に軽減されます。
- 国際的なユーザーへのアクセシビリティが向上します。

IRISを導入することで、開発チームはコア機能の開発により多くの時間を割くことができ、プロジェクト管理の効率が大幅に向上します。

## 📝 更新情報

- **[v0.5.5](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.5.5):** README自動更新処理の改善、英語READMEの更新、ヘッダー画像の更新。 
- [v0.5.4](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.5.4): 英語READMEの更新、SourceSageの設定ファイルのバージョン情報の更新、不要なREADMEの記述の削除、README自動更新機能の改善、いくつかのコード変更。 
- [v0.5.3](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.5.3): READMEの自動更新、タグ付与によるリリースノート作成、英語README作成など、新機能と改善点が追加されました。
- [v0.5.1](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.5.1): ドキュメントと構造を改善し、ユーザーエクスペリエンスを向上させました。
- [v0.5.0](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.5.0): リリースノートの自動生成、READMEの自動更新、ヘッダー画像の生成など、新たな機能が追加されました。
- [v0.4.0](https://github.com/Sunwood-ai-labs/IRIS/releases/tag/v0.4.0): 自動リリースノート生成機能の追加(実験的機能)、GitHub Serviceの改善
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

    alt イシュー管理の自動化
        User->>GitHub: イシューを作成
        GitHub->>IRIS: GitHub Action トリガー
        IRIS->>GitHub: イシュー内容を取得
        GitHub-->>IRIS: イシュー詳細
        IRIS->>AI: 内容を分析リクエスト
        AI-->>IRIS: 分析結果
        IRIS->>Labels: 提案されたラベルを照合
        Labels-->>IRIS: 有効なラベル
        IRIS->>GitHub: 検証済みラベルを適用
        IRIS->>AI: 詳細コメント生成リクエスト
        AI-->>IRIS: 生成された詳細コメント
        IRIS->>GitHub: 詳細コメントを追加
        IRIS->>AI: 変更提案生成リクエスト
        AI-->>IRIS: 生成された変更提案
        IRIS->>GitHub: 変更提案を追加
        GitHub-->>User: イシュー更新通知
    end

    alt リリース管理の自動化
        User->>GitHub: タグを作成/プッシュ
        GitHub->>IRIS: タグイベント通知
        IRIS->>AI: リリースノート生成リクエスト
        AI-->>IRIS: 生成されたリリースノート
        IRIS->>GitHub: リリースノートを作成
        GitHub-->>User: リリース通知
    end

    alt ドキュメンテーションの自動化
        IRIS->>AI: README更新リクエスト
        AI-->>IRIS: 更新されたREADME内容
        IRIS->>GitHub: READMEを更新
        IRIS->>AI: 英語版README生成リクエスト
        AI-->>IRIS: 生成された英語版README
        IRIS->>GitHub: 英語版READMEを追加/更新
        GitHub-->>User: ドキュメント更新通知
    end
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
