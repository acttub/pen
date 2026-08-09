# pen

acttub 디자인 .pen 원본(Pencil, https://pen.dev).

| 파일 | 무엇 |
|---|---|
| `목업v2.pen` | 웹앱 프론트 화면 정본. 데스크톱 D1~D7 · 모바일 M1~M4 등 프레임 37개 |

## 정본은 볼트에 있다
편집은 최우영 로컬 볼트 `Soma/코어/웹/목업v2.pen`에서 하고, 여기엔 사본을 올린다.
갱신하려면 볼트에서 저장한 뒤:

```
cp "$HOME/Soma/코어/웹/목업v2.pen" "$HOME/pen/" && \
  git -C "$HOME/pen" commit -am "목업v2 갱신" && git -C "$HOME/pen" push
```

.pen 은 Pencil 앱으로만 연다(암호화 바이너리, git diff 무의미).
