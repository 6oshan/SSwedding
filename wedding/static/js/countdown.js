const countDownDate = new Date("Nov 23, 2025 11:30:00").getTime();

// Update every second
const timer = setInterval(function () {
    const now = new Date().getTime();
    const distance = countDownDate - now;

    // Time calculations
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the result
    document.getElementById("days").textContent = days;
    document.getElementById("hours").textContent = hours;
    document.getElementById("minutes").textContent = minutes;
    document.getElementById("seconds").textContent = seconds;

    // If countdown is over
    if (distance < 0) {
        clearInterval(timer);
        document.querySelector(".countdown").innerHTML = "<h2>🎉 Countdown Over!</h2>";
    }
}, 1000);


// map Popup

document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('map-modal');
    const btn = document.getElementById('location-btn');
    const closeBtn = document.getElementById('modal-close');

    // Open modal
    btn.addEventListener('click', () => modal.classList.add('active'));

    // Close modal
    closeBtn.addEventListener('click', () => modal.classList.remove('active'));

    // Click outside modal content
    window.addEventListener('click', (e) => {
        if (e.target === modal) modal.classList.remove('active');
    });
});


$(window).scroll(function () {
    if ($(this).scrollTop() > 200) {
        $('#location-btn').addClass('scrolled');
    } else {
        $('#location-btn').removeClass('scrolled');
    }
});

// Select all elements to animate
const animatedElements = document.querySelectorAll('.animate-on-scroll');

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible'); // add visible class
            observer.unobserve(entry.target); // optional: stop observing after animation
        }
    });
}, {
    threshold: 0.1 // triggers when 10% of the element is visible
});

// Observe each element
animatedElements.forEach(el => observer.observe(el));




