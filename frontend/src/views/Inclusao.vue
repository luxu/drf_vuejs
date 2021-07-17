<template>
  <div class="q-pa-md row items-start q-gutter-md justify-center">
    <q-card class="my-card bg-secondary text-white">
      <q-card-section>
        <div class="text-h6 text-center">Bem vindo ao Anexo Semi-Aberto (ASA)</div>
        <div class="text-h6 text-center">{{ title }}</div>
        <div class="text-subtitle2">by {{ developer }}</div>
      </q-card-section>

      <q-separator dark />

      <q-card-section>
        {{ infos }}
      </q-card-section>

      <q-separator dark />

      <q-card-actions class="justify-center">
        <q-btn flat>Raio 1</q-btn>
        <q-btn flat>Raio 2</q-btn>
      </q-card-actions>
    </q-card>

  </div>
</template>

<script>

  import axios from 'axios';

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
    },
    mounted: function() {
      this.FetchData();
    },
    methods: {
        FetchData: function() {
            axios.get("http://localhost:8000/api/user/")
                .then(response => {
                  this.username = response.data.forEach(function(item) {
                      console.log(item['username']);
                  })
            });
        },
        SelectWinner: function() {
          var winner = this.username[Math.floor(Math.random()*this.username.length)];
          this.winner = winner;
        },
    }
  }
</script>

<style lang="sass" scoped>
  .my-card
    width: 100%
    max-width: 250px

</style>
