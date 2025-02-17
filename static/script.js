const ws = new WebSocket("ws://" + location.host + "/ws");

function sendCommand(command) {
    ws.send(JSON.stringify({ action: command }));
}

// Event Listeners for Button Controls
document.getElementById("move-forward").onclick = () => sendCommand("8");
document.getElementById("move-left").onclick = () => sendCommand("4");
document.getElementById("move-right").onclick = () => sendCommand("6");
document.getElementById("move-backward").onclick = () => sendCommand("2");
document.getElementById("stop").onclick = () => sendCommand("5");
document.getElementById("speak").onclick = () => {
    let text = document.getElementById("tts-input").value;
    sendCommand({ speak: text });
};

// 🎮 Gamepad Support
window.addEventListener("gamepadconnected", (event) => {
    console.log("Gamepad connected:", event.gamepad.id);
    setInterval(checkGamepadInput, 100);
});

function checkGamepadInput() {
    let gamepad = navigator.getGamepads()[0];
    if (!gamepad) return;

    let threshold = 0.5;
    if (gamepad.axes[1] < -threshold) sendCommand("8"); // Forward
    else if (gamepad.axes[1] > threshold) sendCommand("2"); // Backward
    else if (gamepad.axes[0] < -threshold) sendCommand("4"); // Left
    else if (gamepad.axes[0] > threshold) sendCommand("6"); // Right
}
