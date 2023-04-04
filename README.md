"# midi" 
magenta 폴더 안에 make_tfrecord.py, train.py, save.py가 있습니다

make_tfrecord.py는 midi data를 tfrecord 파일로 저장하는 코드입니다.
train.py는 tfrecord를 이용하여 학습하는 코드입니다.
save.py는 학습결과를 이용하여 4마디의 드럼 midi 파일을 생성하는 코드입니다.

convert_midi.py는 magenta를 사용하지 않고 dataset을 만드려다가 시간상 힘들 것 같아 보류하고 magenta를 이용하여 문제를 해결했습니다.
