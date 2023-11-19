//시계 기능
function updateTime() {
    const currentTime = new Date();
    let hours = currentTime.getHours();
    const minutes = currentTime.getMinutes();
    const seconds = currentTime.getSeconds();
    let timeString;

    const ampm = hours >= 12 ? '오후' : '오전';
    hours %= 12;
    hours = hours ? hours : 12; // 0시를 12시로 표시

    timeString = `${ampm} ${hours}시 ${minutes < 10 ? '0' + minutes : minutes}분`;
    document.getElementById('current-time').textContent = `현재 시간: ${timeString}`;
    
    // 마우스를 가져다 대었을 때 초를 알려주는 팝업
    document.getElementById('current-time').addEventListener('mouseover', () => {
      const altTimeString = `${ampm} ${hours}시 ${minutes}분 ${seconds}초`;
      document.getElementById('current-time').setAttribute('title', `현재 시간: ${altTimeString}`);
    });
  }

  // 초기 시간 표시
  updateTime();

  // 1초마다 시간 업데이트
  setInterval(updateTime, 1000);

    const menuItems = document.querySelectorAll('.navbar .parent');
  
