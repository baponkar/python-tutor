const snowflakeContainer = document.getElementById('snowflake-container');
const numberOfSnowflakes = 50;

for (let i = 0; i < numberOfSnowflakes; i++) {
    const snowflake = document.createElement('div');
    snowflake.classList.add('snowflake');
    snowflake.innerHTML = '❄';
    snowflake.style.left = `${Math.random() * 100}%`;
    snowflake.style.animationDuration = `${Math.random() * 3 + 2}s`;
    snowflake.style.animationDelay = `${Math.random()}s`;
    snowflake.style.fontSize = `${Math.random() * 5 + 1}px`; // Random font size between 1px and 5px
    snowflakeContainer.appendChild(snowflake);
}