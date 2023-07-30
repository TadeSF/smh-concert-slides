<template>
  <div class="flex flex-col h-full">
    <div class="flex justify-center items-center h-52 overflow-hidden p-8">
      <img class="max-h-full max-w-full" src="../img/logo_inv.svg" alt="Logo" />
    </div>
    <div class="flex-1 flex flex-col justify-center items-center text-center m-10">
      <h1>{{ composer }}</h1>
      <h3 v-if="supertitle">{{ supertitle }}</h3>
      <h2>{{ name }}</h2>
      <h3 v-if="subtitle">{{ subtitle }}</h3>
      <div class="movements">
        <div v-for="(movement, index) in movements" :key="index" :class="currentStep === index ? 'highlight' : 'not-highlight'"
          v-step="index + 1">
          <span class="movement_index" v-if="autoCountMovements">{{ index + 1 }}.</span>
          {{ movement }}
        </div>
      </div>
      <span v-for="(movement, index) in shortenedMovementListForClickCount" :key="index">
        <span v-click></span>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    composer: { type: String, default: '' },
    name: { type: String, default: '' },
    supertitle: { type: String, default: '' },
    subtitle: { type: String, default: '' },
    movements: { type: Array, default: () => [] },
    autoCountMovements: { type: Boolean, default: true },
  },
  computed: {
    currentStep() {
      // The '+' converts the string to a number.
      return +this.$route.query.clicks || 0;
    },
    shortenedMovementListForClickCount() {
      // Shortens the list by 1 for the current click count.
      return this.movements.slice(0, -1);
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
  font-size: 1.5em;
  font-weight: normal;
  margin-top: 0;
}

.highlight {
  transition: all 1s ease-in-out 1s;
  color: #fff;
}
.not-highlight {
  transition: all 1s ease-in-out;
  color: #5c5c5c;
}
.movements {
  margin-top: 1em;
  transition: all 0.5s ease-in-out 1s;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  column-gap: 2em;
  row-gap: 0.5em;
  font-size: 1.3em;
  font-style: italic;
  color: #5c5c5c;
}

.movement_index {
  margin-right: 0.5em;
  font-style: normal;

}

</style>