# 생활코드

    버그
    * 행복한 버그 : 문법오류  
    * 불행한 버그 : 논리적오류 당대에 발견하기 힘들다  
    버전관리는 디버깅 용도  
    * 버전을 잘만든다  
    * 하나의 단위작업이 하나의 버전안에 있을것  
    * 각각의 번전은 그번전을 잘설명할수 있도록 작업내용기술
    * 원하는 버전으로 언제든지 시간여행할수있는 운전능력

## visual studio code 에서 git 사용법

    .git/ 이포함된 폴더 전체를 백업하면 복사본 폴더 복사하면 완벽하게 버전까지 포함해서 복구할 수 있다  

## 1

    work1.txt  1  
    work2.txt  2  
    work3.txt  3  

|working|directory|stageArea||Repository(.git)|||||
|:--:|:--:|:--:|:--:|:---:|:--:|:--:|:--:|:--:|
|name|content|name|content|message|name|content|parent|commitId|
|work1.txt|1|work1.txt|1|work 1|work1.txt|1||201e6c|
|work2.txt|2|work2.txt|2|work 2|work1.txt|1|201e6c|7560cf|
|work3.txt|2|work3.txt|2||work2.txt|2|201e6c|7560cf|
||||||work3.txt|2|201e6c|7560cf|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||

|poister|
|:-----:|
|master|

|master|
|:----:|
|7560cf|

    git config --global user.name "windows_t14"  
    git config --global user.email "kddddds.naver.com"  
    sourtree
    work1.txt A 버튼 stage  
    work1.txt message 1 commit  
    git log
    HEAD -> master -> a  
    work2.txt work3.txt Add work 2 commit  
    git log
    손깃  
    확장프로그램 git graph 하단에 Git Graph

## 버전관리

    work 1 시점으로 이동 
    git checkout 201e6c # 아이디 몇개만 쳐도됨  
    work1.txt만 남고 work2.txt work3.txt 는 삭제  
    Git Graph 도 헤드를 나타내는 동그라미는 work 1 을 가리킴  
    깃은 헤드가 가리키는  
    git log 하면 헤드가 work 2를 가리키고 있기 때문에 work 1 은 보이지 않는다.  
    git log --all 다보임  
    git log --all oneline 간단하게 표시  
    -- 작업후 최신버전으로 바꾸기 현재(마지막버전)으로 돌아와야함  

    master 마지막버전 브랜치에서 마지막버전이 무엇인가 알려줌  

    HEAD 워킹디렉토리와 스테이지에어리어가 어떤 버전이 만들어진 시점의 스테이지와 에어리어가 같은지를 알려줌  
    
    git checkout master # 복구됨

## merge, conflict

    nano f1.txt  
        function(){
            return 'common';
        }  
    git add f1.txt
    git commit -m '1'
    git checkout -b 'exp' # exp 브랜치 만들고 체크아웃까지  
    nano f1.txt
        function(){
            return 'exp';
        }  
    git commit -am 'common->exp'  
    git checkout master  
    nano f1.txt
    nano f1.txt
        function(){
            return 'master';
        }  
    git commit -am 'common -> master'  
    git merge exp # 병합실패 충돌 3way merge  
    nano f1.txt  
        function(){
            <<<<<<< HEAD
                    return 'master';
            =======
                    return 'exp';
            >>>>>>> exp
        }  

    https://sourceforge.net/projects/kdiff3/ # 설치 
    git config --global merge.tool kdiff3  
    git config --global --add mergetool.kdiff3.path "c:/Program Files/KDiff3/kdiff3.exe"  
    git config --global --add mergetool.kdiff3.trustExitCode false



    git mergetool 자동으로 merge 해줌 master 와 exp 수정사항이 공통된 내용 conflict

    a:    function(){
              return 'common';
          }  

    b:    function(){
              return 'master';
          }  

    c:    function(){
              return 'exp';
          }  
    
    Base  
    Local  
    Remote 
    mergetool conflict 부분 수정후 저장 
    git commit -am 'comm -> master'
    git merge exp # 성공

## Remote Repository

    버전백업 협업 중요  
    git init local
    cd local
    nano f1.txt 1
    git add f1.txt
    git commit -m 1
    # 원격저장소에 저장
    cd ..
    git init --bare remote # 벌거벗은 맨살 저장소로서만 기능 수정 불가능 원격저장소 만들때 --bare 옵션
    cd remote
    ls -al
    git remote add origin /home/git/git/remote
    git remote -v
    origin /homegit/git/remote(fetch)
    orgin /home/git/git/remote(push)
    # git config --global push.default matching # 자동
    # git config --global push.default simple # 명시적으로 지정 보수적 엄격
    git config --global push.default simple # simple 방식으로 push
    git push
    git push --set-upstream origin master 
    # push 할때 orgin에 master branch로 push 한다 
    # --set-upstream git push 하면 자동으로 origin master 로 푸시하겠다 로컬브랜치와 원격브랜치 와의 연결을 명시적으로 설정하는 옵션

## Github

    프로젝트 받아오기
        git/git
        commit 
        5branchs
        Fork 복제
        Fork 내페이지에 복사
        clone 주소복사
        mkdir git
        cd git
        git clone http://github.com/ebesesk/git.git gitsrc
        cd gitsrc
        git log --reverse
        # 첫번째 commit
        Initial revision of "git", the information manager from hell
        get checkout e83c5163316f89bfbde7d9ab23ca2e25604af290
    프로젝트 저장하기
        github public 만들기
        repository…or push an existing repository from the command line
            git remote add origin https://github.com/ebesesk/mycode.git
            git branch -M main
            git push -u origin main
        mkdir mycode
        cd mycode
        mkdir asset
        mkdir kimchitv
        git init
        cp kimchi_o.py mycode/kimchi
        git remote add origin https://github.com/ebesesk/mycode.git 
        # git add origin https://github.com/ebesesk/mycode.git origin
        git remote
        -> origin
        git remote -v
        -> origin  https://github.com/ebesesk/mycode.git (fetch)
           origin  https://github.com/ebesesk/mycode.git (push)
        나의 로컬저장소와 연결된 기본 원격저장소
        git remote add mycode http://github.com/ebesesk/mycode.git
        git remote --help
        git remote remove origin
        