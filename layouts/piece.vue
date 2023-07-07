<template>
  <div class="flex flex-col h-full">
    <div class="flex justify-center items-center h-52 overflow-hidden p-8">
      <img class="max-h-full max-w-full" src="../img/logo_inv.svg" alt="Logo" />
    </div>
    <div class="flex-1 flex flex-col justify-center items-center text-center m-10">
      <h1>{{ composer }}</h1>
      <h2>{{ name }}</h2>
      <h3 v-if="subtitle">{{ subtitle }}</h3>
      <div class="movements" :style="`--columns: ${columns};`">
        <div v-for="(movement, index) in movements" :key="index" :class="{ 'highlight': currentStep === index + 1 }"
          v-step="index + 1">
          <span class="movement_index" v-if="autoCountMovements">{{ index + 1 }}.</span>
          {{ movement }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    composer: { type: String, default: '' },
    name: { type: String, default: '' },
    subtitle: { type: String, default: '' },
    movements: { type: Array, default: () => [] },
    columns: { type: Number, default: 1 },
    autoCountMovements: { type: Boolean, default: true },
  },
  computed: {
    currentStep() {
      // The '+' converts the string to a number.
      return +this.$route.query.clicks || 0;
    },
  },
}
</script>

<style scoped>

h1 {
  font-size: 2em;
  /* Uppercase */
  text-transform: uppercase;
  color: #e5013b;
}

h2 {
  font-size: 2em;
  font-weight: bold;
}

h3 {
  font-size: 2em;
  font-weight: normal;
  margin-top: 0;
}

.highlight {
  transition: all 0.5s ease-in-out;
  color: #fff;
}
.movements {
  margin-top: 1em;
  transition: all 0.5s ease-in-out;
  display: grid;
  grid-template-columns: repeat(var(--columns), 1fr);
  gap: 0.5em;
  font-size: 1em;
  font-style: italic;
  color: #888;
}

.movement_index {
  margin: 0 5px;
  font-style: normal;

}

</style>