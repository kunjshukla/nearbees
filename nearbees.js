// menu bar java scipt code
  const menuBtn = document.getElementById('menu-btn');
  const menu = document.getElementById('menu');

  menuBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
  });

  // Close menu when clicking outside of it
  document.addEventListener('click', (event) => {
    const isClickInsideMenu = menu.contains(event.target);
    const isClickInsideMenuBtn = menuBtn.contains(event.target);
    if (!isClickInsideMenu && !isClickInsideMenuBtn) {
      menu.classList.remove('active');
    }
  });
  // image box in the flesh ................................................................................
  function changeImage(imageSrc) {
    var imageElement = document.querySelector('.image');
    imageElement.src = imageSrc;
}
function redirectToNewPage() {
  // Change the location to the URL of the new page
  window.location.href = "upload.html";// here there will be a refrence link to upload page
}
    // Array of image paths
    var images = ['rose01.jpg', 'rose02.jpg', 'sunflower01.jpg']; // Add more images as needed

    var currentIndex = 0;

    // Function to change the image
    function changeImage() {
        var imageElement = document.getElementById('image');
        imageElement.src = images[currentIndex];
        currentIndex = (currentIndex + 1) % images.length; // Cycle through the images
    }

    // Call the changeImage function every 5 seconds
    setInterval(changeImage, 5000);