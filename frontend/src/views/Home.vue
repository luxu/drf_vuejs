<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <q-separator/>
    <div class="q-pa-md q-gutter-sm">
      <q-btn
          color="black"
          label="Incluir Preso"
          size="xl"
          to="/add"
      />
      <q-btn
          color="black"
          label="Excluir Preso"
          size="xl"
          to="/delete"
      />
    </div>
<!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    // HelloWorld
  }
}
</script>
