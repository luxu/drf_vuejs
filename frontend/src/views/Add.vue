<template>
  <div class="q-pa-md" style="max-width: 400px">

    <q-form
      @submit="onSubmit"
      @reset="onReset"
      class="q-gutter-md">
      <q-input
        filled
        v-model="name"
        label="Sentenciado *"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Digite o nome']"
      />

      <q-input
        filled
        v-model="matriculation"
        label="Matricula *"
        lazy-rules
        :rules="[
          val => val && val.length > 0 || 'Digite a matrícula',
        ]"
      />

      <q-input
        filled
        type="date"
        v-model="included"
        label="Data da Inclusão *"
      />

      <div>
        <q-btn label="Submit" type="submit" color="primary"/>
        <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
      </div>
    </q-form>

  </div>
</template>

<script>

export default {
  data () {
    return {
      name: null,
      matriculation: null,
      included: null,
    }
  },

  methods: {
    onSubmit () {
      console.log(this.name)
      },

    onReset () {
      this.name = null
      this.matriculation = null
      this.included = false
    }
  }
}
</script>