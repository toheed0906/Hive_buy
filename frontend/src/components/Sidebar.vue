<template>
    <div class="sidebar">
        <div class="d-flex justify-content-between input-container">
            <div>
                <NumberInput title="Price" :value=0 placeholder="From" unit="$" :full_width=false
                    @input.capture="handleMinimumPrice" />
            </div>
            <div class="pt-5 px-2">
                <span> _ </span>
            </div>
            <div class="pt-4">
                <NumberInput title="" :value=6900 placeholder="To" unit="$" @input.capture="handleMaximumPrice" />
            </div>
        </div>

        <div class="input-container">
            <NumberInput title="MOQ" placeholder="Less Than" :full_width=true
                @input.capture="handleMinimumOrderQauntity" />
        </div>

        <div class="input-container location ">
            <Searchbar title="Manufacturer Location" placeholder="Country/Region" class="pb-4"
                @input.capture="handleLocation" />



            <div v-if="intialCountryLocationToShow != 0">

                <div>
                    <Checkbox v-for="index in intialCountryLocationToShow" :name="countryOptions[index - 1].name"
                        v-model:checked="countryOptions[index - 1].selected" @change="handleManufacturer" />
                </div>
                <div class="pt-3" v-if="intialCountryLocationToShow >= 6">
                    <p v-if="showCompleteLocations" class="see-more-link" @click="showAllLocation()"> Show All ( {{
                        totalCountryLocations }} ) </p>
                    <p v-if="!showCompleteLocations" class="see-more-link" @click="showLessLocations()"> Show Less </p>
                </div>
            </div>
            <div v-if="intialCountryLocationToShow === 0">
                <h2 class="text-center">
                    Nothing To Show
                </h2>
            </div>

        </div>
        <div class="input-container">
            <h3> Stock Availability</h3>
            <Checkbox name="In USA" @change="handleAvailabiltyInUsa"
                v-model:checked="inUSA" />
        </div>
    </div>
</template>

<script setup>
import { ref, onBeforeMount, defineComponent, computed } from 'vue'
import { useStore } from 'vuex'
import NumberInput from '@/components/NumberInput.vue'
import Searchbar from '@/components/Searchbar.vue'
import Checkbox from '@/components/Checkbox.vue'

const store = useStore()
const countryOptions = ref([])
const totalCountryLocations = ref(9)
const intialCountryLocationToShow = ref(7)
const showCompleteLocations = ref(true)
const lengthOfCountry = ref(0)
const selectedLocations = ref('')
const inUSA =ref(store.getters.inUSA);


defineComponent({
    components: {
        Checkbox,
        Searchbar,
        NumberInput
    },
})
onBeforeMount(() => {
    countryOptions.value = [...store.state.country_options]
    lengthOfCountry.value = store.state.country_options.length
})

const handleMinimumPrice = (event) => {
    store.commit('setMinPrice', parseInt(event.target.value) || '');
    store.dispatch('fetchProducts')
}
const handleMaximumPrice = (event) => {
    store.commit('setMaxPrice', parseInt(event.target.value) || '');
    store.dispatch('fetchProducts')
}
const handleMinimumOrderQauntity = (event) => {
    store.commit('setMinimumOrderQuantity', parseInt(event.target.value) || '')
    store.dispatch('fetchProducts')
}
const handleAvailabiltyInUsa = () => {
    if (inUSA.value == false) {
        store.commit('setAvailibityInUsa', '')
    } else {
        store.commit('setAvailibityInUsa', inUSA.value)
    }
    store.dispatch('fetchProducts')
}
const showAllLocation = () => {
    intialCountryLocationToShow.value = totalCountryLocations.value
    showCompleteLocations.value = false
}
const showLessLocations = () => {
    intialCountryLocationToShow.value = 7
    showCompleteLocations.value = true
}

const handleLocation = (event) => {
    let val = event.target.value.toLowerCase()
    countryOptions.value = store.state.country_options.filter(cn => cn.name.toLowerCase().includes(val))
    intialCountryLocationToShow.value = countryOptions.value.length
}
const handleManufacturer = (event) => {
    selectedLocations.value = ''
    for (let i = 0; i < countryOptions.value.length; i++) {
        if (countryOptions.value[i].selected == true) {
            if (selectedLocations.value == '') {
                selectedLocations.value = selectedLocations.value + countryOptions.value[i].name
            } else {
                selectedLocations.value = selectedLocations.value + "," + countryOptions.value[i].name
            }
        }
    }
    store.commit('setManufacturerLocation', selectedLocations.value)
    store.dispatch('fetchProducts')
}
</script>



<style scoped>
.sidebar {
    width: 30%;
    border-width: 1px;
    border-style: solid;
    border-radius: 0.25rem;
    border-color: #e2e8f0;
    margin-top: 12px;
    padding: 20px;
    height: 800px;
}

.input-container {
    padding-top: 32px;
}

.see-more-link {
    text-decoration: underline;
    color: #29b574;
    cursor: pointer;
    margin-bottom: 0;
}

h3 {
    font-size: 1.125rem;
    color: #231f20;
    padding-bottom: 12px;
}

h2 {
    font-size: 1.125rem;
    color: red;
}
</style>