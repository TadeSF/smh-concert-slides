<template>
  <div class="layout">
    <div class="logo">
      <img src="../img/logo_inv.svg" alt="Logo" />
    </div>
    <div class="content" />
  </div>
</template>

<style scoped>
.layout {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.logo {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
  overflow: hidden;
  padding: 2em;

}

.logo img {
  max-height: 100%;
  max-width: 100%;
}

.content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}


</style>