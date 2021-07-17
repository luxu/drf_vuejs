<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/listagem">Listagem de Presos</router-link>
      <div class="text-h6 text-center">Bem vindo ao Anexo Semi-Aberto (ASA)</div>
      <div class="text-h6 text-center">{{ title }}</div>
      <div class="text-subtitle2">by {{ developer }}</div>
    </div>
    <router-view/>
  </div>
</template>

<script>

export default {
    name: 'App',
    data() {
        return {
            username: null,
            winner: null,
            info: '',
            title: 'Alcatraz',
            developer: 'luxu',
            infos: 'Colocar alguma descrição...'
        }
    }
  }
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
