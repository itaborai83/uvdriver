<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <a class="navbar-brand" href="#">UV Driver</a>
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active ">
          <router-link to="/"> Home </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/negative"> Negativo </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/exposure"> Exposição </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/about"> Sobre </router-link>
        </li>
      </ul>
    </nav>
    <router-view/>
  </div>
</template>

<style scoped>
  nav ul li{
    padding: 1rem
  }
</style>
