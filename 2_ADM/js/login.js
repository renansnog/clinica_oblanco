document.getElementById("loginForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const errorMessage = document.getElementById("error-message");

  // Usuário e senha fixos só para teste inicial
  const adminUser = "admin";
  const adminPass = "1234";

  if (username === adminUser && password === adminPass) {
    alert("Login realizado com sucesso!");
    window.location.href = "painel.html"; // Redireciona para painel adm
  } else {
    errorMessage.textContent = "Usuário ou senha incorretos.";
  }
});
