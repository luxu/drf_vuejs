<template>
  <div class="q-pa-md">
    <q-table
      title="Listagem dos Presos do ASA"
      class="my-sticky-header-table"
      :data="data"
      :columns="columns"
      row-key="name"
      bordered
      dark
      color="amber">
    </q-table>
  </div>
</template>

<script>

  import axios from 'axios';

  export default {
    name: 'App',
    data() {
        return {
          data: [],
          columns: [
              {
                name: 'name',
                required: true,
                label: 'Sentenciado',
                align: 'left',
                field: row => row.name,
                format: val => `${val}`,
                sortable: true
              },
              {
                name: 'matriculation',
                label: 'Matrícula',
                align: 'left',
                field: row => row.matriculation,
                format: val => `${val}`,
                sortable: true
              },
              {
                name: 'included',
                label: 'Incluído',
                align: 'left',
                field: row => row.included,
                format: val => `${val}`,
                sortable: true
              },
          ]
        }
    },
    mounted: function() {
      this.FetchData();
    },
    methods: {
        FetchData: function() {
            axios.get("http://localhost:8000/api/sentenciado/")
                .then(response => {
                  this.data = response.data;
                  // this.username = response.data.forEach(function(item) {
                  //     this.data = item;
                  // })
            });
        },
    }
  }
</script>

<style lang="sass" scoped>
  .my-card
    width: 100%
    max-width: 250px

</style>
