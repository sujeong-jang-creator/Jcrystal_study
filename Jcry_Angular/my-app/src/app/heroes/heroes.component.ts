// Agular 컴포넌트를 선언하기 위해서, 반드시 augular core 라이브러리에서 Component 심볼을 로드해야한다.
// import {심볼} from '라이브러리';
import { Component, OnInit } from '@angular/core';
import { Hero } from '../hero';
import { HEROES } from '../mock-heroes';
// 컴포넌트 클래스 지정. @Component
// 컴포넌트 : 템플릿이 존재하는 디렉티브.
// 디렉티브 : Augular 애플리케이션 안에 있는 엘리먼트에 어떤 동작을 추가하는 클래스
@Component({
  // 1. selector : 컴포넌트의 CSS 엘리먼트 셀렉터
  selector: 'app-heroes',
  // 2. templateUrl : 컴포넌트 템플릿 파일 위치
  templateUrl: './heroes.component.html',
  // 3. styleUrls : 컴포넌트 CSS스타일 파일의 위치
  styleUrls: ['./heroes.component.scss']
})
// 컴포넌트는 export(추출)해야 다른 모듈에서 import 가능하다.
export class HeroesComponent implements OnInit {

  heroes = HEROES;
  selectedHero?: Hero;

  constructor() { }

  ngOnInit() {
  }

  onSelect(hero: Hero): void {
    this.selectedHero = hero;
  }

  // ngOnInit : 라이프싸이클 후킹함수 > angular의 라이프싸이클에 간섭하는(영향을 미치는) 함수.
  // hooking : OS나 응용 소프트웨어 등 각종 컴퓨터 프로그램에서 소프트웨어 구성 요소간에 발생하는 함수호출, 메세지, 이벤트 등을 중간에서 바꾸거나 가로채는 명령, 방법, 기술, 행위.
  //          이때 이렇게 간섭된 함수호출, 이벤트, 메세지 등을 처리하는 코드를 훅이라고 한다. 빼돌리거나 간섭하는 코드.
}
