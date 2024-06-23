<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/IRIS.png" width="100%">
<br>
<h1 align="center">IRIS</h1>
<h2 align="center">
  ～ Intelligent Repository Issue Solver ～
<br>
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/IRIS">
<img alt="PyPI - Format" src="https://img.shields.io/pypi/format/IRIS">
<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/IRIS">
<img alt="PyPI - Status" src="https://img.shields.io/pypi/status/IRIS">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/IRIS">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/IRIS">
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

# I.R.I.S（Intelligent Repository Issue Solver）

## 🌟 はじめに

I.R.I.S（Intelligent Repository Issue Solver）は、GitHubリポジトリのイシュー管理を劇的に向上させるインテリジェントアシスタントです。機械学習と自然言語処理を活用し、イシューの自動分類、優先順位付け、解決策の提案を行います。

## 🚀 機能

- イシューの自動ラベリング
- OpenAI GPT-4を使用したイシュー分析
- GitHubアクションを通じた自動化プロセス

## 🛠️ インストールと設定

1. このリポジトリをクローンまたはフォークします。
2. `.github/workflows/issue-review.yml`ファイルをあなたのリポジトリの`.github/workflows/`ディレクトリにコピーします。
3. GitHub SecretsにOpenAI APIキー（`OPENAI_API_KEY`）とGitHubアクセストークン（`GH_ACCESS_TOKEN`）を設定します。

## 🔧 使用方法

I.R.I.Sは新しいイシューが作成されると自動的に起動します。以下のプロセスが実行されます：

1. イシューの内容を分析
2. 適切なラベルを提案
3. 提案されたラベルをイシューに適用
4. ラベリング結果をコメントとして追加

## 📝 更新情報

- バージョン1.0.0: 初期リリース
- イシュー自動ラベリング機能の実装

## 🤝 コントリビューション

プロジェクトへの貢献を歓迎します！以下の方法で貢献できます：

1. イシューを作成して改善点や問題点を報告
2. 新機能の提案
3. プルリクエストを送信してコードを改善

## 📄 ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。

## 🙏 謝辞

- OpenAI - GPT-4の提供
- GitHub - アクションと開発プラットフォームの提供
- すべてのコントリビューターとユーザーの皆様


```bash
aira --mode=commit --config=.aira\config.IRIS.yml
```

```bash
sourcesage --yaml-file=docs\.sourcesage_releasenotes.yml
```



```mermaid
%%{init:{'theme':'base','themeVariables':{'primaryColor':'#024959','primaryTextColor':'#F2C335','primaryBorderColor':'#F2AE30','lineColor':'#A1A2A6','secondaryColor':'#593E25','tertiaryColor':'#F2C335','noteTextColor':'#024959','noteBkgColor':'#F2C335','textColor':'#024959','fontSize':'18px'}}}%%

sequenceDiagram
    participant 👤 as 🌟User
    participant 🐙 as 🐙GitHub
    participant 🤖 as 🤖I.R.I.S
    participant 🧠 as 🧠GPT-4
    
    👤->>🐙: 🎫 新しいイシューを作成
    🐙->>🤖: 🚀 GitHub Action トリガー
    activate 🤖
    🤖->>🐙: 📥 イシュー内容を取得
    🐙-->>🤖: 📄 イシュー詳細
    🤖->>🧠: 🔍 内容を分析リクエスト
    activate 🧠
    🧠-->>🤖: 🏷️ ラベル提案
    deactivate 🧠
    🤖->>🐙: 🔖 ラベルを適用
    🤖->>🐙: 💬 コメントを追加
    deactivate 🤖
    🐙-->>👤: 📨 更新通知
```

