<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="glossy">
      <q-toolbar>

        <q-toolbar-title>
          Penitenciária de Presidente Prudente
        </q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <Inicio />
    </q-page-container>
  </q-layout>
</template>

<script>
// import HelloWorld from './components/Index.vue'
import Inicio from './components/Index.vue'

export default {
  name: 'LayoutDefault',
  components: {
    Inicio
  },
  data () {
    return {

    }
  }
}
</script>

<style>
</style>
