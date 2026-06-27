
import {Fragment,memo,useContext,useEffect} from "react"
import {isTrue} from "$/utils/state"
import {StateContexts} from "$/utils/context"
import {jsx} from "@emotion/react"






export const Cond_comp_fe57df97a27d7859fff6f3004f6b6f36 = memo(({children}) => {
    const reflex___state____state__api_programas___api_programas____state = useContext(StateContexts.reflex___state____state__api_programas___api_programas____state)



    return(
        (reflex___state____state__api_programas___api_programas____state.cargando_rx_state_?(children?.at?.(0)):(children?.at?.(1)))
    )
});
