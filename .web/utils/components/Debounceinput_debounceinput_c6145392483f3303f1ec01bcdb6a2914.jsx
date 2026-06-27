
import {Fragment,memo,useCallback,useContext,useEffect} from "react"
import {ReflexEvent,applyEventActions,isTrue} from "$/utils/state"
import DebounceInput from "react-debounce-input"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {TextArea as RadixThemesTextArea} from "@radix-ui/themes"
import {jsx} from "@emotion/react"






export const Debounceinput_debounceinput_c6145392483f3303f1ec01bcdb6a2914 = memo(({children}) => {
    const [addEvents, connectErrors] = useContext(EventLoopContext);
const on_change_ac6060fb98c41c7bb9981e1d27020968 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.api_programas___api_programas____state.set_pregunta", ({ ["valor"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])
const reflex___state____state__api_programas___api_programas____state = useContext(StateContexts.reflex___state____state__api_programas___api_programas____state)



    return(
        jsx(DebounceInput,{debounceTimeout:300,element:RadixThemesTextArea,onChange:on_change_ac6060fb98c41c7bb9981e1d27020968,placeholder:"Escribe tu consulta...",value:reflex___state____state__api_programas___api_programas____state.pregunta_rx_state_},)
    )
});
