
import {Fragment,memo,useCallback,useContext,useEffect} from "react"
import {ReflexEvent,applyEventActions,isTrue} from "$/utils/state"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {jsx} from "@emotion/react"






export const Textarea_textarea_e34361b72aea8447316e835a9889c82b = memo(({children}) => {
    const [addEvents, connectErrors] = useContext(EventLoopContext);
const on_change_ac6060fb98c41c7bb9981e1d27020968 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.api_programas___api_programas____state.set_pregunta", ({ ["valor"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])
const reflex___state____state__api_programas___api_programas____state = useContext(StateContexts.reflex___state____state__api_programas___api_programas____state)



    return(
        jsx("textarea",{onChange:on_change_ac6060fb98c41c7bb9981e1d27020968,placeholder:"Escribe tu pregunta sobre propietarios, mascotas o consultas veterinarias...",value:reflex___state____state__api_programas___api_programas____state.pregunta_rx_state_},)
    )
});
