# SWsummerproject_surfing_game

#python_이용한_surfing_game


-pygame 모듈 이용
명령프롬프트 pip install pygame

-database - firebase 이용하여 최대 거리 기록 저장

#프로젝트 일정[간트차트]
![간트차트](https://user-images.githubusercontent.com/43884708/125405738-ffe94300-e3f2-11eb-86b8-ffadfc26b224.JPG)

#프로젝트 제안서[ppt]
[복사본 서핑게임_20184429_김수빈.pptx](https://github.com/tabss2003/SWsummerproject_surfing_game/files/6806544/_20184429_.pptx)


#프로젝트 중간 변경사항[ppt]
[중간발표 서핑게임_20184429_김수빈.pptx](https://github.com/tabss2003/SWsummerproject_surfing_game/files/6837885/_20184429_.pptx)

#최종 결과
[intro]
![intro](https://user-images.githubusercontent.com/43884708/126646679-1e684251-70d6-495c-a992-51f657dd2a24.JPG)

◎게임 룰

-캐릭터의 생명 = trash_pass 와 같다.

-trash_pass = 0 에서 시작을 하며, trash_pass =5가 될 경우 GAMEOVER

-최대 거리기록제로 제일 멀리 간 기록을 RANK을 누르면 확인할 수 있다.

-거리는 0M에서 시작한다.


[RANK]
![RANKbutton](https://user-images.githubusercontent.com/43884708/126647793-0ce72f71-23e2-4cad-b672-0253b651f5e6.JPG)


[START_게임화면]

※방향키, 스페이스 바를 이용

※왼쪽 상단에 trash_pass =0, 0M가 표시되어 있다.

-방향키로 캐릭터(서핑보드)를 움직여 장애물(쓰레기,파도)을 피한다.

-스페이스 바를 이용하여 장애물(쓰레기)를 공격하여 없앤다.

-장애물(쓰레기)를 없애지 못하고 장애물이 화면에서 사라질 경우 trash_pass(즉,캐릭터의 생명) +1 씩 증가한다

-장애물(쓰레기,파도)에 부딪힐 경우 Crashed ! 표시와 함께 2-3초뒤에 게임이 재시작된다.

![space](https://user-images.githubusercontent.com/43884708/126646755-4e5421dd-2801-4cbe-9362-22a4f81ae067.JPG)


![crashed](https://user-images.githubusercontent.com/43884708/126648178-a187569f-2535-455c-8659-6570613622f5.JPG)

[GAMEOVER]

-GAMEOVER 표시와 함께 데이터베이스에 저장된 최대 거리를 확인할 수 있다.

-GAMEOVER 표시 3초 뒤에 intro 화면으로 전환된다.

![gameover](https://user-images.githubusercontent.com/43884708/126647966-6738e907-9363-4e04-b510-8632845113e8.JPG)


![firebase_db](https://user-images.githubusercontent.com/43884708/126647983-a9f7a7b3-bb0d-457a-889f-7d9257c8ce5c.JPG)

