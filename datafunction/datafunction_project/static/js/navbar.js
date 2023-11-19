
menuItems.forEach((item) => {
    const submenu = item.querySelector('.submenu');

    item.addEventListener('click', (event) => {
      submenu.style.display = submenu.style.display === 'block' ? 'none' : 'block';

      menuItems.forEach((otherItem) => {
        if (otherItem !== item) {
          otherItem.querySelector('.submenu').style.display = 'none';
        }
      });

      event.stopPropagation();
    });

    document.addEventListener('click', (event) => {
      const isClickInside = item.contains(event.target);
      if (!isClickInside) {
        submenu.style.display = 'none';
      }
    });

    // 클릭 시 배경색 변경
    item.addEventListener('mousedown', () => {
      item.style.backgroundColor = '#3d3f54';
    });

    item.addEventListener('mouseup', () => {
      item.style.backgroundColor = 'transparent';
    });
  });

  document.addEventListener('click', (event) => {
  const isClickInside = hamburgerIcon.contains(event.target);
  if (!isClickInside) {
    submenu.style.display = 'none';
  }
});
