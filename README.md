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

### 작성자 정보 넣기

    git config --global user.name code-server
    git config --global user.email kddddds@naver.com
    git init    # 현재 디렉토리 버전관리 프로젝트 폴더 지정
        # .git 폴더 생성 버전관리 정보 저장 디렉토리
        # f1.txt 만들고 source : 1 넣기
    git status
        Untracked files:
            f1.txt
    git add f1.txt  git f1.txt 추적하라고 명령
        Change to be committed:
            new file:   f1.txt
    git commit   # nano 실행 됨 정보 알려주는곳 현재 버전 메세지 입력 1입력
    git log  # 입력한 내용 출력
        f1.txt  수정 source : 2
    git status
        Changes not staged for commit:
            modified: f1.txt
    git add f1.txt  # 다시 버전관리 하기 최초만들고 add 수정하고나서도 add
    git commit      # 2 입력 변경이류 적는곳
    git log         # 버전정보 나옴

    nano f2.txt     # f2.txt 만들고 source : 1 입력
    git add f2.txt
    git commit      # 버전정보 넣기 source : 1

    # f1.txt f2.txt 모두 수정
    # f1.txt f1.txt : 2     f2.txt f2.txt : 2
    git status 
        Changes not staged for commit:
        (use "git add <file>..." to update what will be committed)
        (use "git restore <file>..." to discard changes in working directory)
                modified:   f1.txt
                modified:   f2.txt

    git add f1.txt
    git status
        Changes to be committed:
        (use "git restore --staged <file>..." to unstage)
                modified:   f1.txt

        Changes not staged for commit:  # 커밋이 되지않을것이다 add한 파일만 commit
        (use "git add <file>..." to update what will be committed)
        (use "git restore <file>..." to discard changes in working directory)
                modified:   f2.txt
        # 커밋할 파일만 선택해서 커밋할수 있다
        # 커밋 대기상태 staged area
        # stage 커밋을대기하기위해 가는곳 
        # repository 커밋되어 저장되어지는곳

    # 차이점을 알수있고 
    # 과거로 돌아갈수 있다
    git log -p # 커밋 사이의 소스 차이점을 알수있다

        commit 7c02410672182ef8d9a2b36385d37699db323220 (HEAD -> master)
        Author: code-server <kddddds@naver.com>
        Date:   Wed Feb 9 02:57:27 2022 +0900

            4[f1.txt] # 가장마지막

        diff --git a/f1.txt b/f1.txt
        index 2456b16..9462317 100644
        --- a/f1.txt    # 3[f2.txt] 에서의 파일내용             # 3과 4사이의 차이점
        +++ b/f1.txt    # 4[f1.txt] 파일내용
        @@ -1 +1 @@
        -source : 2     # 3[f2.txt] 에서의 파일내용
        +f1.txt : 2     # 4[f1.txt] 파일내용

        commit 3dc4577e807ea74af5b57c069f9f65871bf24bc7
        Author: code-server <kddddds@naver.com>
        Date:   Wed Feb 9 02:48:47 2022 +0900

            3[f2.txt]

        diff --git a/f2.txt b/f2.txt
        new file mode 100644
        index 0000000..2456b16
        --- /dev/null   # 이전에선 존재하지 않았음
        +++ b/f2.txt    # 현재버전에서 f2.txt 파일 추가됨
        @@ -0,0 +1 @@
        +source : 2     # 내용은 source2 였음

        commit 90786cd623d42140476dc8e83de74028fd96c8f8
        Author: code-server <kddddds@naver.com>
        Date:   Wed Feb 9 02:31:31 2022 +0900

            2[f1.txt]

        diff --git a/f1.txt b/f1.txt
        index e2eaf76..2456b16 100644
        --- a/f1.txt    # 이전버전에도 존재
        +++ b/f1.txt    # 현재버전에도 존재
        @@ -1 +1 @@
        -source : 1     # 이전버전에선 source 1
        +source : 2     # 현재 버전에선 source 2

        commit ef3e3161899b8773277140321b488449a85fd257 # 커밋의 고유아이디
        Author: code-server <kddddds@naver.com>
        Date:   Wed Feb 9 02:30:38 2022 +0900

            1[f1.txt]

        diff --git a/f1.txt b/f1.txt
        new file mode 100644
        index 0000000..e2eaf76
        --- /dev/null
        +++ b/f1.txt
        @@ -0,0 +1 @@
        +source : 1

    git diff ef3e3161899b8773277140321b488449a85fd257

    nano f1.txt # f1.txt 파일수정
    git diff # 커밋하기전 변경내용 리뷰
        index 9462317..e3a30dc 100644
        --- a/f1.txt
        +++ b/f1.txt
        @@ -1 +1 @@
        -f1.txt : 2     # 변경내용 확인
        +f1.txt : 5
        diff --git a/f2.txt b/f2.txt

    git add f1.txt
    git commit
    git log -p


    # 과거로 되돌리기
    # reset VS revert
    # 관리하는 디렉토리 .git/ 포함 백업후 작업
        cp -pR /config/workspace/git_ebesesk/생활코딩/. /config/workspace/git_ebesesk/생활코딩2/
            -h 심볼릭 링크파일 복사
            -p 파일권한 복사
            -R 하위 디렉토리 복사

    5 와 4를 삭제하고 3으로 돌아가고싶다 reset
    git reset 3dc4577e807ea74af5b57c069f9f65871bf24bc7 --hard <- 3번째 아이디 4, 5 삭제됨

        commit 64dda4ca82014a50f73877d66660135a9261be2a (HEAD -> master)
        Author: code-server <kddddds@naver.com>
        Date:   Wed Feb 9 10:24:57 2022 +0900

            5[f1.txt]

        commit 7c02410672182ef8d9a2b36385d37699db323220
        Author: code-server <kddddds@naver.com>
        Date:   Wed Feb 9 02:57:27 2022 +0900

            4[f1.txt]

        commit 3dc4577e807ea74af5b57c069f9f65871bf24bc7
        Author: code-server <kddddds@naver.com>
        Date:   Wed Feb 9 02:48:47 2022 +0900

            3[f2.txt]

        commit 90786cd623d42140476dc8e83de74028fd96c8f8
        Author: code-server <kddddds@naver.com>
        Date:   Wed Feb 9 02:31:31 2022 +0900

            2[f1.txt]

        commit ef3e3161899b8773277140321b488449a85fd257
        Author: code-server <kddddds@naver.com>
        Date:   Wed Feb 9 02:30:38 2022 +0900

            1[f1.txt]

    # 버전 4 5 삭제한것처럼 보이지만 데이터는 남아있다.
    # 원격저장소 협업 저장소 버전들을 공유 reset 하면 안됨
    git revert 3dc4577e807ea74af5b57c069f9f65871bf24bc7 <- 커밋취소하면서 새로 버전 만듦

    # git 명령어 빈도수
        # commit
        push
        pull
        # clone
        checkout
        # add
        branch
        # log
        # diff
        fetch
        merge
        # init
        # status
        # reset
        # revert
    nano f1.txt
    git add f1.txt
    git commit
    #########################################################
    git commit --amend      #가장 최근의 commit 메세지 수정
    git rebase -i HEAD~3    # 위에서 세번째 커밋 메세지 수정
    git reset HEAD~1        # 가장 최근 commit 삭제
    git commit -a           # add명령어 없이 자동으로 add
    git commit -am "11"     # 자동 add, 에디터없이 메세지 넣을수있음
    ##########################################################
    # 버전관리하는 이유 백업 backup
    # 버전관리하는 디렉토리 클라우드 서비스에 올리기 인터넷상에 저장

## 2

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
        repository
        …or push an existing repository from the command line
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
        git remote add origin http://github.com/ebesesk/mycode.git
        git remote --help
        git branch -M main
        git push -u origin main
        # -u 옵션 로컬저장소  branch 와 원격저장소 마스터 branch를 연결해서 다음부턴 자동으로 넘어감 한번만 실행
        git commit -am "README.md 추가"
    다운받기
        mkdir mycode
        cd mycode
        git clone https://github.com/ebesesk/mycode.git .
