
import {Fragment,memo,useContext,useEffect} from "react"
import {isTrue} from "$/utils/state"
import {StateContexts} from "$/utils/context"
import {jsx} from "@emotion/react"






export const Bare_comp_ce8882e3304115fc98bcea1c32b1c7a9 = memo(({children}) => {
    const reflex___state____state__api_programas___api_programas____state = useContext(StateContexts.reflex___state____state__api_programas___api_programas____state)



    return(
        (reflex___state____state__api_programas___api_programas____state.cargando_rx_state_ ? "Consultando la base de datos..." : reflex___state____state__api_programas___api_programas____state.respuesta_rx_state_)
    )
});
