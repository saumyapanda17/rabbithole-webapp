/* eslint-disable */
<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link :to="{ name: 'home' }" class="navbar-brand"
        >rabbithole
      </router-link>

      <div id="navbarSupportedContent" class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <router-link :to="{ name: 'home' }" class="btn btn-dark"
              >Home
            </router-link>
          </li>
          <li class="nav-item mx-1">
            <router-link :to="{ name: 'question-editor' }" class="btn btn-dark"
              >Ask Question
            </router-link>
          </li>
          <li class="nav-item">
            <a class="btn btn-outline-dark" href="/accounts/logout/">Logout </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent",
};
</script>

<style>
.my-navbar {
  border-bottom: 3px solid rgb(215, 206, 206);
}

.navbar-brand {
  font-weight: bold;
  font-size: 230%;
  color: rgb(160, 42, 81) !important;
}

.navbar-brand:hover {
  color: rgb(182, 45, 91) !important;
}
</style>
