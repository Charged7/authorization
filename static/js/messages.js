// Автоматическое удаление сообщений через 3 секунды
    document.addEventListener('DOMContentLoaded', function() {
        console.log("Messages js connected")
        const alerts = document.querySelectorAll('.messages-container .alert');
        alerts.forEach(function(alert) {
            setTimeout(function() {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }, 2000);
        });
    });