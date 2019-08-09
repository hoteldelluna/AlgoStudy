# Python Algorithm Study

<img src="https://img.shields.io/badge/language-python-blue">

### 규칙

1. **`master` branch는 건드리지 않습니다.**

2. **`dev` branch 권한은 운영진들만 가집니다.**

   > dev는 작성하는 공간이 아닌 merge를 띄워 서로의 내용들을 모아두는 공간입니다.
   >
   > master는 이후 어느정도 되었다 하였을 때, 배포한다는 느낌으로 두는 공간으로 낫둡니다.

3. **자신의 브런치 생성 이름 :point_right: `python/깃허브닉네임`**

   > 개인당 최대 2개의 branch를 사용할 수 있습니다. (단, 운영진 제외)
   >
   > 잘못된 branch가 보일 경우에는 바로 삭제하겠습니다.
   >
   > 너무 많은 branch를 사용할 경우 난잡해지기 때문이니 양해부탁드립니다.
   >
   > branch명을 통일하는 것은 branch사용법과 협업을 연습하기 위함입니다.
   >
   > brach명은 `python/깃허브닉네임`, `temp/깃허브닉네임`입니다.
   >
   > **python/**은 자신의 소스를 올리고 merge를 하기 위한 공간이며,
   >
   > **temp/**은 혹여나 `python/`의 오류가 발생할 수도 있기에 여유분의 공간입니다.
   >
   > 2개의 branch가 오류가 났을 경우에는 문의를 주시기 바랍니다.

4. **폴더 관리:point_right:root폴더/`깃허브닉네임`/폴더**

   > **example)**
   >
   > 백준, SW expert academy, 정올...etc가 있을 때,
   >
   > `root폴더(깃저장소처음공간)/TaeJuneJoung/acm/p1260.py`
   >
   > 이런식으로 가지게 됩니다.
   >
   > 다른 사람들이 `acm`이라고 하면 잘 모를 수 있으므로 `TaeJuneJoung`폴더를 들어갔을 때 바로 readMe파일을 통해 어떻게 관리되고 있는지 작성해주세요.

5. **Merge 필수**

   > 자신이 푼 문제에 대해서 자신의 branch에 올리고 난 후에는 dev branch에 merge를 꼭 해주세요.
   >
   > 가능하면 Commit을 연습하기 위해 한 문제를 풀고 난 후, git add하고 commit을 해당 문제와 연관하여 해주세요.
   >
   > **example)**
   >
   > 백준 p1260문제를 풀었다고 하였을 때,
   >
   > ```bash
   > $ git add TaeJuneJoung/acm/p1260.py
   > $ git commit -m "p1260 백준 DFS&BFS"
   > ```

6. **문제풀이과정 기재**

   > 문제를 어떠한 사고로 풀었는지 주석으로 작성하여 주세요.
   >
   > ```python
   > """
   > [P01]1부터 10의 숫자를 더해주는 문제라고 가정
   > 1~10을 하나씩 탐색하면 o(1)이 10번 해지기에 등차수열의 합 공식 이용
   > """
   > N = int(input())
   > print(n*(n+1)/2)
   > ```



### P.S.

​	정말 번거로운 작업들이 많이 있다는 것을 알고 있으나, 협업에서 가장 기초적이면서도 중요한 과정입니다. 문서작업과 기재는 다른 사람들이 보고 정리도 잘하고 실력있는 개발자라는 것을 증명해주기도 하지만 무엇보다 이후에 나에게 도움이 될 것입니다.

​	계속 공부해 나가야하는 개발자이기에 Input이 생기는 만큼 Output도 생기기에 **미래의 나를 위해 투자**하신다고 생각해주시길 바랍니다.

​	좋은 곳에서 다시 볼 날을 위해:crossed_fingers: