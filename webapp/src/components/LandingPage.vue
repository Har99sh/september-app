<template>
    <div>
        <span>{{hello}}</span>
        <input type="text" name="" id="" v-model="hello">
    </div>
</template>

<script>
export default {
    data() {
        return {
            "hello": "",
        }
    }
}
</script>
