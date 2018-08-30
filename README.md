# FOXのinputプログラムについて

## FOX_onlyCamera
これは、Kinectのカメラ入力でスケルトン化していないWebカメラの入力がそのまま出るものである。
<br>
FOXで人の顔を撮影するときに使う。

## FOX_onlySkeleton
これは、Kinectのカメラ入力からスケルトン化させるものである。
<br>
FOXで両腕の幅を測定するときに使う。

## FOX_test
上記の二つをまとめたものである。キーボードの"p"を押して写真撮影が可能。

## FOX_python_input
音声の読み上げに対してシーンの切り替えを行うものである。
<br>
`Port番号は12345`
<br>
`IPは127.0.0.1`
<br>
OSC messageは"/event_state"で数値が渡された時を考えている。

## FOX_osc_test.maxpat
FOX_python_inputとの連携で簡単に動作確認を行うことができるものである。

## FOX_voice.py
"Hey,FOX"でイベントが起動し、音声読み上げがスタートしFOX_python_inputのシーンの切り替えが行えるようにするものである。
音声ファイルはvoiceファイルに全て入っている。

## visionAPI_test.py
cloud visionAPIを叩き、４つの感情を返ってくるものをテストできるものである。
<br>
`$ python visionAPI_test.py img1.jpg`
<br>
のように記述する必要がある。エラーを吐く場合は、IPアドレスが異なる場合で、googleのプロジェクトを設定し直す必要がある。

## cvapi.py
cloud visionAPIをうまく叩けているか確認するものである。
<br>
`$ python visionAPI_test.py api_key img1.jpg`
<br>
のように記述する必要がある。エラーを吐く場合、エラーに記述されているIPアドレスをコピーし、プロジェクトに設定する必要がある。


