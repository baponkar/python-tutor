const animatedText = document.getElementById('animatedText');
    const text = animatedText.textContent; // Get the text content of the div
    const delay = 100; // Delay between each character (in milliseconds)

    animatedText.textContent = ''; // Clear the text content of the div

    // Function to animate text
    function animateText(text, index) {
    if (index < text.length) {
        animatedText.textContent += text.charAt(index);
        index++;
        setTimeout(function() {
        animateText(text, index);
        }, delay);
    }
    }

    // Start the animation
    animateText(text, 0);